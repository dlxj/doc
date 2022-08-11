# DB/concern/config.py
import importlib
from collections import OrderedDict

import anyconfig
import munch


class Config(object):
    def __init__(self):
        pass

    def load(self, conf):
        conf = anyconfig.load(conf)
        return munch.munchify(conf)

    def compile(self, conf, return_packages=False):
        packages = conf.get('package', [])
        defines = {}

        for path in conf.get('import', []):
            parent_conf = self.load(path)
            parent_packages, parent_defines = self.compile(
                parent_conf, return_packages=True)
            packages.extend(parent_packages)
            defines.update(parent_defines)

        modules = []
        for package in packages:
            module = importlib.import_module(package)
            modules.append(module)

        if isinstance(conf['define'], dict):
            conf['define'] = [conf['define']]

        for define in conf['define']:
            name = define.copy().pop('name')

            if not isinstance(name, str):
                raise RuntimeError('name must be str')

            defines[name] = self.compile_conf(define, defines, modules)

        if return_packages:
            return packages, defines
        else:
            return defines

    def compile_conf(self, conf, defines, modules):
        if isinstance(conf, (int, float)):
            return conf
        elif isinstance(conf, str):
            if conf.startswith('^'):
                return defines[conf[1:]]
            if conf.startswith('$'):
                return {'class': self.find_class_in_modules(conf[1:], modules)}
            return conf
        elif isinstance(conf, dict):
            if 'class' in conf:
                conf['class'] = self.find_class_in_modules(
                    conf['class'], modules)
            if 'base' in conf:
                base = conf.copy().pop('base')

                if not isinstance(base, str):
                    raise RuntimeError('base must be str')

                conf = {
                    **defines[base],
                    **conf,
                }
            return {key: self.compile_conf(value, defines, modules) for key, value in conf.items()}
        elif isinstance(conf, (list, tuple)):
            return [self.compile_conf(value, defines, modules) for value in conf]
        else:
            return conf

    def find_class_in_modules(self, cls, modules):
        if not isinstance(cls, str):
            raise RuntimeError('class name must be str')

        if cls.find('.') != -1:
            package, cls = cls.rsplit('.', 1)
            module = importlib.import_module(package)
            if hasattr(module, cls):
                return module.__name__ + '.' + cls

        for module in modules:
            if hasattr(module, cls):
                return module.__name__ + '.' + cls
        raise RuntimeError('class not found ' + cls)


class State:
    def __init__(self, autoload=True, default=None):
        self.autoload = autoload
        self.default = default


class StateMeta(type):
    def __new__(mcs, name, bases, attrs):
        current_states = []
        for key, value in attrs.items():
            if isinstance(value, State):
                current_states.append((key, value))

        current_states.sort(key=lambda x: x[0])
        attrs['states'] = OrderedDict(current_states)
        new_class = super(StateMeta, mcs).__new__(mcs, name, bases, attrs)

        # Walk through the MRO
        states = OrderedDict()
        for base in reversed(new_class.__mro__):
            if hasattr(base, 'states'):
                states.update(base.states)
        new_class.states = states

        for key, value in states.items():
            setattr(new_class, key, value.default)

        return new_class


class Configurable(metaclass=StateMeta):
    def __init__(self, *args, cmd={}, **kwargs):
        self.load_all(cmd=cmd, **kwargs)

    @staticmethod
    def construct_class_from_config(args):
        cls = Configurable.extract_class_from_args(args)
        return cls(**args)

    @staticmethod
    def extract_class_from_args(args):
        cls = args.copy().pop('class')
        package, cls = cls.rsplit('.', 1)
        module = importlib.import_module(package)
        cls = getattr(module, cls)
        return cls

    def load_all(self, **kwargs):
        for name, state in self.states.items():
            if state.autoload:
                self.load(name, **kwargs)

    def load(self, state_name, **kwargs):
        # FIXME: kwargs should be filtered
        # Args passed from command line
        cmd = kwargs.pop('cmd', dict())
        if state_name in kwargs:
            setattr(self, state_name, self.create_member_from_config(
                (kwargs[state_name], cmd)))
        else:
            setattr(self, state_name, self.states[state_name].default)

    def create_member_from_config(self, conf):
        args, cmd = conf
        if args is None or isinstance(args, (int, float, str)):
            return args
        elif isinstance(args, (list, tuple)):
            return [self.create_member_from_config((subargs, cmd)) for subargs in args]
        elif isinstance(args, dict):
            if 'class' in args:
                cls = self.extract_class_from_args(args)
                return cls(**args, cmd=cmd)
            return {key: self.create_member_from_config((subargs, cmd)) for key, subargs in args.items()}
        else:
            return args

    def dump(self):
        state = {}
        state['class'] = self.__class__.__module__ + \
            '.' + self.__class__.__name__
        for name, value in self.states.items():
            obj = getattr(self, name)
            state[name] = self.dump_obj(obj)
        return state

    def dump_obj(self, obj):
        if obj is None:
            return None
        elif hasattr(obj, 'dump'):
            return obj.dump()
        elif isinstance(obj, (int, float, str)):
            return obj
        elif isinstance(obj, (list, tuple)):
            return [self.dump_obj(value) for value in obj]
        elif isinstance(obj, dict):
            return {key: self.dump_obj(value) for key, value in obj.items()}
        else:
            return str(obj)


# DB/concern/log.py
import os
import logging
import functools
import json
import time
from datetime import datetime

from tensorboardX import SummaryWriter
import yaml
import cv2
import numpy as np

# from concern.config import Configurable, State


class Logger(Configurable):
    SUMMARY_DIR_NAME = 'summaries'
    VISUALIZE_NAME = 'visualize'
    LOG_FILE_NAME = 'output.log'
    ARGS_FILE_NAME = 'args.log'
    METRICS_FILE_NAME = 'metrics.log'

    database_dir = State(default='./outputs/')
    log_dir = State(default='workspace')
    verbose = State(default=False)
    level = State(default='info')
    log_interval = State(default=100)

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

        self._make_storage()

        cmd = kwargs['cmd']
        self.name = cmd['name']
        self.log_dir = os.path.join(self.log_dir, self.name)
        try:
            self.verbose = cmd['verbose']
        except:
            print('verbose:', self.verbose)
        if self.verbose:
            print('Initializing log dir for', self.log_dir)

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        self.message_logger = self._init_message_logger()

        summary_path = os.path.join(self.log_dir, self.SUMMARY_DIR_NAME)
        self.tf_board_logger = SummaryWriter(summary_path)

        self.metrics_writer = open(os.path.join(
            self.log_dir, self.METRICS_FILE_NAME), 'at')

        self.timestamp = time.time()
        self.logged = -1
        self.speed = None
        self.eta_time = None

    def _make_storage(self):
        application = os.path.basename(os.getcwd())
        storage_dir = os.path.join(
            self.database_dir, self.log_dir, application)
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        if not os.path.exists(self.log_dir):
            os.symlink(storage_dir, self.log_dir)

    def save_dir(self, dir_name):
        return os.path.join(self.log_dir, dir_name)

    def _init_message_logger(self):
        message_logger = logging.getLogger('messages')
        message_logger.setLevel(
            logging.DEBUG if self.verbose else logging.INFO)
        formatter = logging.Formatter(
            '[%(levelname)s] [%(asctime)s] %(message)s')
        std_handler = logging.StreamHandler()
        std_handler.setLevel(message_logger.level)
        std_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(
            os.path.join(self.log_dir, self.LOG_FILE_NAME))
        file_handler.setLevel(message_logger.level)
        file_handler.setFormatter(formatter)

        message_logger.addHandler(std_handler)
        message_logger.addHandler(file_handler)
        return message_logger

    def report_time(self, name: str):
        if self.verbose:
            self.info(name + " time :" + str(time.time() - self.timestamp))
            self.timestamp = time.time()

    def report_eta(self, steps, total, epoch):
        self.logged = self.logged % total + 1
        steps = steps % total
        if self.eta_time is None:
            self.eta_time = time.time()
            speed = -1
        else:
            eta_time = time.time()
            speed = eta_time - self.eta_time
            if self.speed is not None:
                speed = ((self.logged - 1) * self.speed + speed) / self.logged
            self.speed = speed
            self.eta_time = eta_time

        seconds = (total - steps) * speed
        hours = seconds // 3600
        minutes = (seconds - (hours * 3600)) // 60
        seconds = seconds % 60

        print('%d/%d batches processed in epoch %d, ETA: %2d:%2d:%2d' %
              (steps, total, epoch,
               hours, minutes, seconds), end='\r')

    def args(self, parameters=None):
        if parameters is None:
            with open(os.path.join(self.log_dir, self.ARGS_FILE_NAME), 'rt') as reader:
                return yaml.load(reader.read())
        with open(os.path.join(self.log_dir, self.ARGS_FILE_NAME), 'wt') as writer:
            yaml.dump(parameters.dump(), writer)

    def metrics(self, epoch, steps, metrics_dict):
        results = {}
        for name, a in metrics_dict.items():
            results[name] = {'count': a.count, 'value': float(a.avg)}
            self.add_scalar('metrics/' + name, a.avg, steps)
        result_dict = {
            str(datetime.now()): {
                'epoch': epoch,
                'steps': steps,
                **results
            }
        }
        string_result = yaml.dump(result_dict)
        self.info(string_result)
        self.metrics_writer.write(string_result)
        self.metrics_writer.flush()

    def named_number(self, name, num=None, default=0):
        if num is None:
            return int(self.has_signal(name)) or default
        else:
            with open(os.path.join(self.log_dir, name), 'w') as writer:
                writer.write(str(num))
            return num

    epoch = functools.partialmethod(named_number, 'epoch')
    iter = functools.partialmethod(named_number, 'iter')

    def message(self, level, content):
        self.message_logger.__getattribute__(level)(content)

    def images(self, prefix, image_dict, step):
        for name, image in image_dict.items():
            self.add_image(prefix + '/' + name, image, step, dataformats='HWC')

    def merge_save_images(self, name, images):
        for i, image in enumerate(images):
            if i == 0:
                result = image
            else:
                result = np.concatenate([result, image], 0)
        cv2.imwrite(os.path.join(self.vis_dir(), name+'.jpg'), result)

    def vis_dir(self):
        vis_dir = os.path.join(self.log_dir, self.VISUALIZE_NAME)
        if not os.path.exists(vis_dir):
            os.mkdir(vis_dir)
        return vis_dir

    def save_image_dict(self, images, max_size=1024):
        for file_name, image in images.items():
            height, width = image.shape[:2]
            if height > width:
                actual_height = min(height, max_size)
                actual_width = int(round(actual_height * width / height))
            else:
                actual_width = min(width, max_size)
                actual_height = int(round(actual_width * height / width))
                image = cv2.resize(image, (actual_width, actual_height))
            cv2.imwrite(os.path.join(self.vis_dir(), file_name+'.jpg'), image)

    def __getattr__(self, name):
        message_levels = set(['debug', 'info', 'warning', 'error', 'critical'])
        if name == '__setstate__':
            raise AttributeError('haha')
        if name in message_levels:
            return functools.partial(self.message, name)
        elif hasattr(self.__dict__.get('tf_board_logger'), name):
            return self.tf_board_logger.__getattribute__(name)
        else:
            super()

import torch.nn as nn
import math
import torch.utils.model_zoo as model_zoo
BatchNorm2d = nn.BatchNorm2d

model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
}


def constant_init(module, constant, bias=0):
    nn.init.constant_(module.weight, constant)
    if hasattr(module, 'bias'):
        nn.init.constant_(module.bias, bias)


def conv3x3(in_planes, out_planes, stride=1):
    """3x3 convolution with padding"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)


class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsample=None, dcn=None):
        super(BasicBlock, self).__init__()
        self.with_dcn = dcn is not None
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace=True)
        self.with_modulated_dcn = False
        if self.with_dcn:
            fallback_on_stride = dcn.get('fallback_on_stride', False)
            self.with_modulated_dcn = dcn.get('modulated', False)
        # self.conv2 = conv3x3(planes, planes)
        if not self.with_dcn or fallback_on_stride:
            self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
                                   padding=1, bias=False)
        else:
            deformable_groups = dcn.get('deformable_groups', 1)
            if not self.with_modulated_dcn:
                # from assets.ops.dcn import DeformConv
                from dcn import DeformConv
                conv_op = DeformConv
                offset_channels = 18
            else:
                # from assets.ops.dcn import ModulatedDeformConv
                from dcn import ModulatedDeformConv
                conv_op = ModulatedDeformConv
                offset_channels = 27
            self.conv2_offset = nn.Conv2d(
                planes,
                deformable_groups * offset_channels,
                kernel_size=3,
                padding=1)
            self.conv2 = conv_op(
                planes,
                planes,
                kernel_size=3,
                padding=1,
                deformable_groups=deformable_groups,
                bias=False)
        self.bn2 = BatchNorm2d(planes)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        # out = self.conv2(out)
        if not self.with_dcn:
            out = self.conv2(out)
        elif self.with_modulated_dcn:
            offset_mask = self.conv2_offset(out)
            offset = offset_mask[:, :18, :, :]
            mask = offset_mask[:, -9:, :, :].sigmoid()
            out = self.conv2(out, offset, mask)
        else:
            offset = self.conv2_offset(out)
            out = self.conv2(out, offset)
        out = self.bn2(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out


class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inplanes, planes, stride=1, downsample=None, dcn=None):
        super(Bottleneck, self).__init__()
        self.with_dcn = dcn is not None
        self.conv1 = nn.Conv2d(inplanes, planes, kernel_size=1, bias=False)
        self.bn1 = BatchNorm2d(planes)
        fallback_on_stride = False
        self.with_modulated_dcn = False
        if self.with_dcn:
            fallback_on_stride = dcn.get('fallback_on_stride', False)
            self.with_modulated_dcn = dcn.get('modulated', False)
        if not self.with_dcn or fallback_on_stride:
            self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
                                   stride=stride, padding=1, bias=False)
        else:
            deformable_groups = dcn.get('deformable_groups', 1)
            if not self.with_modulated_dcn:
                from assets.ops.dcn import DeformConv
                conv_op = DeformConv
                offset_channels = 18
            else:
                from assets.ops.dcn import ModulatedDeformConv
                conv_op = ModulatedDeformConv
                offset_channels = 27
            self.conv2_offset = nn.Conv2d(
                planes, deformable_groups * offset_channels,
                kernel_size=3,
                padding=1)
            self.conv2 = conv_op(
                planes, planes, kernel_size=3, padding=1, stride=stride,
                deformable_groups=deformable_groups, bias=False)
        self.bn2 = BatchNorm2d(planes)
        self.conv3 = nn.Conv2d(planes, planes * 4, kernel_size=1, bias=False)
        self.bn3 = BatchNorm2d(planes * 4)
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample
        self.stride = stride
        self.dcn = dcn
        self.with_dcn = dcn is not None

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        # out = self.conv2(out)
        if not self.with_dcn:
            out = self.conv2(out)
        elif self.with_modulated_dcn:
            offset_mask = self.conv2_offset(out)
            offset = offset_mask[:, :18, :, :]
            mask = offset_mask[:, -9:, :, :].sigmoid()
            out = self.conv2(out, offset, mask)
        else:
            offset = self.conv2_offset(out)
            out = self.conv2(out, offset)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out


class ResNet(nn.Module):
    def __init__(self, block, layers, num_classes=1000, 
                 dcn=None, stage_with_dcn=(False, False, False, False)):
        self.dcn = dcn
        self.stage_with_dcn = stage_with_dcn
        self.inplanes = 64
        super(ResNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3,
                               bias=False)
        self.bn1 = BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(
            block, 128, layers[1], stride=2, dcn=dcn)
        self.layer3 = self._make_layer(
            block, 256, layers[2], stride=2, dcn=dcn)
        self.layer4 = self._make_layer(
            block, 512, layers[3], stride=2, dcn=dcn)
        self.avgpool = nn.AvgPool2d(7, stride=1)
        self.fc = nn.Linear(512 * block.expansion, num_classes)
    
        self.smooth = nn.Conv2d(2048, 256, kernel_size=1, stride=1, padding=1)    

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
        if self.dcn is not None:
            for m in self.modules():
                if isinstance(m, Bottleneck) or isinstance(m, BasicBlock):
                    if hasattr(m, 'conv2_offset'):
                        constant_init(m.conv2_offset, 0)

    def _make_layer(self, block, planes, blocks, stride=1, dcn=None):
        downsample = None
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.inplanes, planes * block.expansion,
                          kernel_size=1, stride=stride, bias=False),
                BatchNorm2d(planes * block.expansion),
            )

        layers = []
        layers.append(block(self.inplanes, planes,
                            stride, downsample, dcn=dcn))
        self.inplanes = planes * block.expansion
        for i in range(1, blocks):
            layers.append(block(self.inplanes, planes, dcn=dcn))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x2 = self.layer1(x)
        x3 = self.layer2(x2)
        x4 = self.layer3(x3)
        x5 = self.layer4(x4)

        return x2, x3, x4, x5


def resnet18(pretrained=True, **kwargs):
    """Constructs a ResNet-18 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [2, 2, 2, 2], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet18']), strict=False)
    return model

def deformable_resnet18(pretrained=True, **kwargs):
    """Constructs a ResNet-18 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [2, 2, 2, 2],
                    dcn=dict(modulated=True,
                            deformable_groups=1,
                            fallback_on_stride=False),
                    stage_with_dcn=[False, True, True, True], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet18']), strict=False)
    return model


def resnet34(pretrained=True, **kwargs):
    """Constructs a ResNet-34 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [3, 4, 6, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet34']), strict=False)
    return model


def resnet50(pretrained=True, **kwargs):
    """Constructs a ResNet-50 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet50']), strict=False)
    return model


def deformable_resnet50(pretrained=True, **kwargs):
    """Constructs a ResNet-50 model with deformable conv.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 6, 3],
                   dcn=dict(modulated=True,
                            deformable_groups=1,
                            fallback_on_stride=False),
                   stage_with_dcn=[False, True, True, True],
                   **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet50']), strict=False)
    return model


def resnet101(pretrained=True, **kwargs):
    """Constructs a ResNet-101 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 23, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet101']), strict=False)
    return model


def resnet152(pretrained=True, **kwargs):
    """Constructs a ResNet-152 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 8, 36, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet152']), strict=False)
    return model


# DB/structure/model.py
import os

import torch
import torch.nn as nn
import torch.nn.functional as F

#import backbones
#import decoders


class BasicModel(nn.Module):
    def __init__(self, args):
        nn.Module.__init__(self)

        #self.backbone = getattr(backbones, args['backbone'])(**args.get('backbone_args', {}))
        backboneName = 'deformable_resnet18' # args['backbone']
        backboneFunc = deformable_resnet18 #getattr(backbones, backboneName)
        backboneInstance = backboneFunc(**args.get('backbone_args', {}))
        self.backbone = backboneInstance

        self.decoder = getattr(decoders, args['decoder'])(**args.get('decoder_args', {}))

    def forward(self, data, *args, **kwargs):
        return self.decoder(self.backbone(data), *args, **kwargs)


def parallelize(model, distributed, local_rank):
    if distributed:
        return nn.parallel.DistributedDataParallel(
            model,
            device_ids=[local_rank],
            output_device=[local_rank],
            find_unused_parameters=True)
    else:
        return nn.DataParallel(model)

class SegDetectorModel(nn.Module):
    def __init__(self, args, device, distributed: bool = False, local_rank: int = 0):
        super(SegDetectorModel, self).__init__()
        from decoders.seg_detector_loss import SegDetectorLossBuilder

        self.model = BasicModel(args)
        # for loading models
        self.model = parallelize(self.model, distributed, local_rank)
        self.criterion = SegDetectorLossBuilder(
            args['loss_class'], *args.get('loss_args', []), **args.get('loss_kwargs', {})).build()
        self.criterion = parallelize(self.criterion, distributed, local_rank)
        self.device = device
        self.to(self.device)

    @staticmethod
    def model_name(args):
        return os.path.join('seg_detector', args['backbone'], args['loss_class'])

    def forward(self, batch, training=True):
        if isinstance(batch, dict):
            data = batch['image'].to(self.device)
        else:
            data = batch.to(self.device)
        data = data.float()
        pred = self.model(data, training=self.training)

        if self.training:
            for key, value in batch.items():
                if value is not None:
                    if hasattr(value, 'to'):
                        batch[key] = value.to(self.device)
            loss_with_metrics = self.criterion(pred, batch)
            loss, metrics = loss_with_metrics
            return loss, pred, metrics
        return pred


# DB/experiment.py
#from concern.config import Configurable, State
# from concern.log import Logger
# from structure.builder import Builder
# from structure.representers import *
# from structure.measurers import *
# from structure.visualizers import *
# from data.data_loader import *
# from data import *
# from training.model_saver import ModelSaver
# from training.checkpoint import Checkpoint
# from training.optimizer_scheduler import OptimizerScheduler


class Structure(Configurable):
    builder = State()
    representer = State()
    measurer = State()
    visualizer = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

    @property
    def model_name(self):
        return self.builder.model_name


class TrainSettings(Configurable):
    data_loader = State()
    model_saver = State()
    checkpoint = State()
    scheduler = State()
    epochs = State(default=10)

    def __init__(self, **kwargs):
        kwargs['cmd'].update(is_train=True)
        self.load_all(**kwargs)
        if 'epochs' in kwargs['cmd']:
            self.epochs = kwargs['cmd']['epochs']


class ValidationSettings(Configurable):
    data_loaders = State()
    visualize = State()
    interval = State(default=100)
    exempt = State(default=-1)

    def __init__(self, **kwargs):
        kwargs['cmd'].update(is_train=False)
        self.load_all(**kwargs)

        cmd = kwargs['cmd']
        self.visualize = cmd['visualize']


class EvaluationSettings(Configurable):
    data_loaders = State()
    visualize = State(default=True)
    resume = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)


class EvaluationSettings2(Configurable):
    structure = State()
    data_loaders = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)


class ShowSettings(Configurable):
    data_loader = State()
    representer = State()
    visualizer = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)


class Experiment(Configurable):
    structure = State(autoload=False)
    train = State()
    validation = State(autoload=False)
    evaluation = State(autoload=False)
    logger = State(autoload=True)

    def __init__(self, **kwargs):
        self.load('structure', **kwargs)

        cmd = kwargs.get('cmd', {})
        if 'name' not in cmd:
            cmd['name'] = self.structure.model_name

        self.load_all(**kwargs)
        self.distributed = cmd.get('distributed', False)
        self.local_rank = cmd.get('local_rank', 0)

        if cmd.get('validate', False):
            self.load('validation', **kwargs)
        else:
            self.validation = None



import os

import torch
from tqdm import tqdm

# from experiment import Experiment
# from data.data_loader import DistributedSampler


class Trainer:
    def __init__(self, experiment: Experiment):
        self.init_device()

        self.experiment = experiment
        self.structure = experiment.structure
        self.logger = experiment.logger
        self.model_saver = experiment.train.model_saver

        # FIXME: Hack the save model path into logger path
        self.model_saver.dir_path = self.logger.save_dir(
            self.model_saver.dir_path)
        self.current_lr = 0

        self.total = 0

    def init_device(self):
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')

    def init_model(self):
        model = self.structure.builder.build(
            self.device, self.experiment.distributed, self.experiment.local_rank)
        return model

    def update_learning_rate(self, optimizer, epoch, step):
        lr = self.experiment.train.scheduler.learning_rate.get_learning_rate(
            epoch, step)

        for group in optimizer.param_groups:
            group['lr'] = lr
        self.current_lr = lr

    def train(self):
        self.logger.report_time('Start')
        self.logger.args(self.experiment)
        model = self.init_model()
        train_data_loader = self.experiment.train.data_loader
        if self.experiment.validation:
            validation_loaders = self.experiment.validation.data_loaders

        self.steps = 0
        if self.experiment.train.checkpoint:
            self.experiment.train.checkpoint.restore_model(
                model, self.device, self.logger)
            epoch, iter_delta = self.experiment.train.checkpoint.restore_counter()
            self.steps = epoch * self.total + iter_delta

        # Init start epoch and iter
        optimizer = self.experiment.train.scheduler.create_optimizer(
            model.parameters())

        self.logger.report_time('Init')

        model.train()
        while True:
            self.logger.info('Training epoch ' + str(epoch))
            self.logger.epoch(epoch)
            self.total = len(train_data_loader)

            for batch in train_data_loader:
                self.update_learning_rate(optimizer, epoch, self.steps)

                self.logger.report_time("Data loading")

                if self.experiment.validation and\
                        self.steps % self.experiment.validation.interval == 0 and\
                        self.steps > self.experiment.validation.exempt:
                    self.validate(validation_loaders, model, epoch, self.steps)
                self.logger.report_time('Validating ')
                if self.logger.verbose:
                    torch.cuda.synchronize()

                self.train_step(model, optimizer, batch,
                                epoch=epoch, step=self.steps)
                if self.logger.verbose:
                    torch.cuda.synchronize()
                self.logger.report_time('Forwarding ')

                self.model_saver.maybe_save_model(
                    model, epoch, self.steps, self.logger)

                self.steps += 1
                self.logger.report_eta(self.steps, self.total, epoch)

            epoch += 1
            if epoch > self.experiment.train.epochs:
                self.model_saver.save_checkpoint(model, 'final')
                if self.experiment.validation:
                    self.validate(validation_loaders, model, epoch, self.steps)
                self.logger.info('Training done')
                break
            iter_delta = 0

    def train_step(self, model, optimizer, batch, epoch, step, **kwards):
        optimizer.zero_grad()

        results = model.forward(batch, training=True)
        if len(results) == 2:
            l, pred = results
            metrics = {}
        elif len(results) == 3:
            l, pred, metrics = results

        if isinstance(l, dict):
            line = []
            loss = torch.tensor(0.).cuda()
            for key, l_val in l.items():
                loss += l_val.mean()
                line.append('loss_{0}:{1:.4f}'.format(key, l_val.mean()))
        else:
            loss = l.mean()
        loss.backward()
        optimizer.step()

        if step % self.experiment.logger.log_interval == 0:
            if isinstance(l, dict):
                line = '\t'.join(line)
                log_info = '\t'.join(['step:{:6d}', 'epoch:{:3d}', '{}', 'lr:{:.4f}']).format(step, epoch, line, self.current_lr)
                self.logger.info(log_info)
            else:
                self.logger.info('step: %6d, epoch: %3d, loss: %.6f, lr: %f' % (
                    step, epoch, loss.item(), self.current_lr))
            self.logger.add_scalar('loss', loss, step)
            self.logger.add_scalar('learning_rate', self.current_lr, step)
            for name, metric in metrics.items():
                self.logger.add_scalar(name, metric.mean(), step)
                self.logger.info('%s: %6f' % (name, metric.mean()))

            self.logger.report_time('Logging')

    def validate(self, validation_loaders, model, epoch, step):
        all_matircs = {}
        model.eval()
        for name, loader in validation_loaders.items():
            if self.experiment.validation.visualize:
                metrics, vis_images = self.validate_step(
                    loader, model, True)
                self.logger.images(
                    os.path.join('vis', name), vis_images, step)
            else:
                metrics, vis_images = self.validate_step(loader, model, False)
            for _key, metric in metrics.items():
                key = name + '/' + _key
                if key in all_matircs:
                    all_matircs[key].update(metric.val, metric.count)
                else:
                    all_matircs[key] = metric

        for key, metric in all_matircs.items():
            self.logger.info('%s : %f (%d)' % (key, metric.avg, metric.count))
        self.logger.metrics(epoch, self.steps, all_matircs)
        model.train()
        return all_matircs

    def validate_step(self, data_loader, model, visualize=False):
        raw_metrics = []
        vis_images = dict()
        for i, batch in tqdm(enumerate(data_loader), total=len(data_loader)):
            pred = model.forward(batch, training=False)
            output = self.structure.representer.represent(batch, pred)
            raw_metric, interested = self.structure.measurer.validate_measure(
                batch, output)
            raw_metrics.append(raw_metric)

            if visualize and self.structure.visualizer:
                vis_image = self.structure.visualizer.visualize(
                    batch, output, interested)
                vis_images.update(vis_image)
        metrics = self.structure.measurer.gather_measure(
            raw_metrics, self.logger)
        return metrics, vis_images

    def to_np(self, x):
        return x.cpu().data.numpy()






# #!python3
import argparse
import time

import torch
import yaml

# # from trainer import Trainer
# # # tagged yaml objects
# # from experiment import Structure, TrainSettings, ValidationSettings, Experiment
# # from concern.log import Logger
# # from data.data_loader import DataLoader
# # from data.image_dataset import ImageDataset
# # from training.checkpoint import Checkpoint
# # from training.model_saver import ModelSaver
# # from training.optimizer_scheduler import OptimizerScheduler
# # from concern.config import Configurable, Config

import sys

def main():
    # """
    # CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1
    # """
    # #sys.argv.append( 'experiments/seg_detector/td500_resnet18_deform_thre.yaml' )
    # # sys.argv.append( '/content/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml' )

    # sys.argv.append( '--num_gpus' )
    # sys.argv.append( '1' )

    # parser = argparse.ArgumentParser(description='Text Recognition Training')
    # parser.add_argument('exp', default='/content/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml', type=str)
    # parser.add_argument('--name', type=str)
    # parser.add_argument('--batch_size', type=int, help='Batch size for training')
    # parser.add_argument('--resume', type=str, help='Resume from checkpoint')
    # parser.add_argument('--epochs', type=int, help='Number of training epochs')
    # parser.add_argument('--num_workers', type=int, help='Number of dataloader workers')
    # parser.add_argument('--start_iter', type=int, help='Begin counting iterations starting from this value (should be used with resume)')
    # parser.add_argument('--start_epoch', type=int, help='Begin counting epoch starting from this value (should be used with resume)')
    # parser.add_argument('--max_size', type=int, help='max length of label')
    # parser.add_argument('--lr', type=float, help='initial learning rate')
    # parser.add_argument('--optimizer', type=str, help='The optimizer want to use')
    # parser.add_argument('--thresh', type=float, help='The threshold to replace it in the representers')
    # parser.add_argument('--verbose', action='store_true', help='show verbose info')
    # parser.add_argument('--visualize', action='store_true', help='visualize maps in tensorboard')
    # parser.add_argument('--force_reload', action='store_true', dest='force_reload', help='Force reload data meta')
    # parser.add_argument('--no-force_reload', action='store_false', dest='force_reload', help='Force reload data meta')
    # parser.add_argument('--validate', action='store_true', dest='validate', help='Validate during training')
    # parser.add_argument('--no-validate', action='store_false', dest='validate', help='Validate during training')
    # parser.add_argument('--print-config-only', action='store_true', help='print config without actual training')
    # parser.add_argument('--debug', action='store_true', dest='debug', help='Run with debug mode, which hacks dataset num_samples to toy number')
    # parser.add_argument('--no-debug', action='store_false', dest='debug', help='Run without debug mode')
    # parser.add_argument('--benchmark', action='store_true', dest='benchmark', help='Open cudnn benchmark mode')
    # parser.add_argument('--no-benchmark', action='store_false', dest='benchmark', help='Turn cudnn benchmark mode off')
    # parser.add_argument('-d', '--distributed', action='store_true', dest='distributed', help='Use distributed training')
    # parser.add_argument('--local_rank', dest='local_rank', default=0, type=int, help='Use distributed training')
    # parser.add_argument('-g', '--num_gpus', dest='num_gpus', default=4, type=int, help='The number of accessible gpus')
    # parser.set_defaults(debug=False)
    # parser.set_defaults(benchmark=True)

    # args = parser.parse_args()
    # args = vars(args)
    # args = {k: v for k, v in args.items() if v is not None}

#     if args['distributed']:
#         torch.cuda.set_device(args['local_rank'])
#         torch.distributed.init_process_group(backend='nccl', init_method='env://')

    args = {
        'exp': '/content/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml',
        'verbose': False,
        'visualize': False,
        'force_reload': False,
        'validate': False,
        'print_config_only': False,
        'debug': False,
        'benchmark': True,
        'distributed': False,
        'local_rank': 0,
        'num_gpus': 1,
    }

    conf = Config()
    experiment_args = conf.compile(conf.load(args['exp']))['Experiment']
    experiment_args.update(cmd=args)
    experiment = Configurable.construct_class_from_config(experiment_args)

    if not args['print_config_only']:
        torch.backends.cudnn.benchmark = args['benchmark']
        trainer = Trainer(experiment)
        trainer.train()

if __name__ == '__main__':
    main()



# """

# CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1

# """