#!python3
import argparse
from asyncio.windows_events import NULL
import time

import torch
import yaml

from trainer import Trainer
# tagged yaml objects
from experiment import Structure, TrainSettings, ValidationSettings, Experiment
from concern.log import Logger
from data.data_loader import DataLoader
from data.image_dataset import ImageDataset
from training.checkpoint import Checkpoint
from training.model_saver import ModelSaver
from training.optimizer_scheduler import OptimizerScheduler
from concern.config import Configurable, Config

import json
import decimal
import datetime


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)


def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()


def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json


def parse(s):
    return json.loads(s, strict=False)

# convert dict to string


def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


def main():

    import sys
    sys.argv.append('experiments/seg_detector/td500_resnet18_deform_thre.yaml')
    sys.argv.append('--num_gpus')
    sys.argv.append('1')
    # torch.backends.cudnn.enabled = False

    parser = argparse.ArgumentParser(description='Text Recognition Training')
    parser.add_argument('exp', type=str)
    parser.add_argument('--name', type=str)
    parser.add_argument('--batch_size', type=int,
                        help='Batch size for training')
    parser.add_argument('--resume', type=str, help='Resume from checkpoint')
    parser.add_argument('--epochs', type=int, help='Number of training epochs')
    parser.add_argument('--num_workers', type=int,
                        help='Number of dataloader workers')
    parser.add_argument('--start_iter', type=int,
                        help='Begin counting iterations starting from this value (should be used with resume)')
    parser.add_argument('--start_epoch', type=int,
                        help='Begin counting epoch starting from this value (should be used with resume)')
    parser.add_argument('--max_size', type=int, help='max length of label')
    parser.add_argument('--lr', type=float, help='initial learning rate')
    parser.add_argument('--optimizer', type=str,
                        help='The optimizer want to use')
    parser.add_argument('--thresh', type=float,
                        help='The threshold to replace it in the representers')
    parser.add_argument('--verbose', action='store_true',
                        help='show verbose info')
    parser.add_argument('--visualize', action='store_true',
                        help='visualize maps in tensorboard')
    parser.add_argument('--force_reload', action='store_true',
                        dest='force_reload', help='Force reload data meta')
    parser.add_argument('--no-force_reload', action='store_false',
                        dest='force_reload', help='Force reload data meta')
    parser.add_argument('--validate', action='store_true',
                        dest='validate', help='Validate during training')
    parser.add_argument('--no-validate', action='store_false',
                        dest='validate', help='Validate during training')
    parser.add_argument('--print-config-only', action='store_true',
                        help='print config without actual training')
    parser.add_argument('--debug', action='store_true', dest='debug',
                        help='Run with debug mode, which hacks dataset num_samples to toy number')
    parser.add_argument('--no-debug', action='store_false',
                        dest='debug', help='Run without debug mode')
    parser.add_argument('--benchmark', action='store_true',
                        dest='benchmark', help='Open cudnn benchmark mode')
    parser.add_argument('--no-benchmark', action='store_false',
                        dest='benchmark', help='Turn cudnn benchmark mode off')
    parser.add_argument('-d', '--distributed', action='store_true',
                        dest='distributed', help='Use distributed training')
    parser.add_argument('--local_rank', dest='local_rank',
                        default=0, type=int, help='Use distributed training')
    parser.add_argument('-g', '--num_gpus', dest='num_gpus',
                        default=4, type=int, help='The number of accessible gpus')
    parser.set_defaults(debug=False)
    parser.set_defaults(benchmark=True)

    args = parser.parse_args()
    args = vars(args)
    args = {k: v for k, v in args.items() if v is not None}

    if args['distributed']:
        torch.cuda.set_device(args['local_rank'])
        torch.distributed.init_process_group(
            backend='nccl', init_method='env://')

    # conf = Config()
    # experiment_args = conf.compile(conf.load(args['exp']))['Experiment']
    # experiment_args.update(cmd=args)
    # save_json('./experiment_args.json', experiment_args)

    experiment_args = {
        "name": "Experiment",
        "class": "experiment.Experiment",
        "structure": {
            "class": "experiment.Structure",
            "builder": {
                "class": "experiment.Builder",
                "model": "SegDetectorModel",
                "model_args": {
                    "backbone": "deformable_resnet18",
                    "decoder": "SegDetector",
                    "decoder_args": {
                        "adaptive": True,
                        "in_channels": [
                            64,
                            128,
                            256,
                            512
                        ],
                        "k": 50
                    },
                    "loss_class": "L1BalanceCELoss"
                }
            },
            "representer": {
                "class": "experiment.SegDetectorRepresenter",
                "max_candidates": 1000
            },
            "measurer": {
                "class": "experiment.QuadMeasurer"
            },
            "visualizer": {
                "class": "experiment.SegDetectorVisualizer"
            }
        },
        "train": {
            "class": "experiment.TrainSettings",
            "data_loader": {
                "class": "experiment.DataLoader",
                "dataset": {
                    "name": "train_data",
                    "class": "experiment.ImageDataset",
                    "data_dir": [
                        "./datasets/TD_TR/TD500/",
                        "./datasets/TD_TR/TR400/"
                    ],
                    "data_list": [
                        "./datasets/TD_TR/TD500/train_list.txt",
                        "./datasets/TD_TR/TR400/train_list.txt"
                    ],
                    "processes": [
                        {
                            "class": "data.processes.AugmentDetectionData",
                            "augmenter_args": [
                                [
                                    "Fliplr",
                                    0.5
                                ],
                                {
                                    "cls": "Affine",
                                    "rotate": [
                                        -10,
                                        10
                                    ]
                                },
                                [
                                    "Resize",
                                    [
                                        0.5,
                                        3.0
                                    ]
                                ]
                            ],
                            "only_resize": False,
                            "keep_ratio": False
                        },
                        {
                            "class": "data.processes.RandomCropData",
                            "size": [
                                640,
                                640
                            ],
                            "max_tries": 10
                        },
                        {
                            "class": "data.processes.MakeICDARData"
                        },
                        {
                            "class": "data.processes.MakeSegDetectionData"
                        },
                        {
                            "class": "experiment.MakeBorderMap"
                        },
                        {
                            "class": "data.processes.NormalizeImage"
                        },
                        {
                            "class": "data.processes.FilterKeys",
                            "superfluous": [
                                "polygons",
                                "filename",
                                "shape",
                                "ignore_tags",
                                "is_training"
                            ]
                        }
                    ]
                },
                "batch_size": 16,
                "num_workers": 16
            },
            "checkpoint": {
                "class": "experiment.Checkpoint",
                "start_epoch": 0,
                "start_iter": 0,
                "resume": NULL
            },
            "model_saver": {
                "class": "experiment.ModelSaver",
                "dir_path": "model",
                "save_interval": 18000,
                "signal_path": "save"
            },
            "scheduler": {
                "class": "experiment.OptimizerScheduler",
                "optimizer": "SGD",
                "optimizer_args": {
                    "lr": 0.007,
                    "momentum": 0.9,
                    "weight_decay": 0.0001
                },
                "learning_rate": {
                    "class": "training.learning_rate.DecayLearningRate",
                    "epochs": 1200
                }
            },
            "epochs": 1200
        },
        "validation": {
            "class": "experiment.ValidationSettings",
            "data_loaders": {
                "icdar2015": {
                    "class": "experiment.DataLoader",
                    "dataset": {
                        "name": "validate_data",
                        "class": "experiment.ImageDataset",
                        "data_dir": [
                            "./datasets/TD_TR/TD500/"
                        ],
                        "data_list": [
                            "./datasets/TD_TR/TD500/test_list.txt"
                        ],
                        "processes": [
                            {
                                "class": "data.processes.AugmentDetectionData",
                                "augmenter_args": [
                                    [
                                        "Resize",
                                        {
                                            "width": 736,
                                            "height": 736
                                        }
                                    ]
                                ],
                                "only_resize": True,
                                "keep_ratio": True
                            },
                            {
                                "class": "data.processes.MakeICDARData"
                            },
                            {
                                "class": "data.processes.MakeSegDetectionData"
                            },
                            {
                                "class": "data.processes.NormalizeImage"
                            }
                        ]
                    },
                    "batch_size": 1,
                    "num_workers": 16,
                    "collect_fn": {
                        "class": "data.processes.ICDARCollectFN"
                    }
                }
            },
            "visualize": False,
            "interval": 4500,
            "exempt": 1
        },
        "logger": {
            "class": "experiment.Logger",
            "verbose": True,
            "level": "info",
            "log_interval": 450
        },
        "evaluation": {
            "class": "experiment.ValidationSettings",
            "data_loaders": {
                "icdar2015": {
                    "class": "experiment.DataLoader",
                    "dataset": {
                        "name": "validate_data",
                        "class": "experiment.ImageDataset",
                        "data_dir": [
                            "./datasets/TD_TR/TD500/"
                        ],
                        "data_list": [
                            "./datasets/TD_TR/TD500/test_list.txt"
                        ],
                        "processes": [
                            {
                                "class": "data.processes.AugmentDetectionData",
                                "augmenter_args": [
                                    [
                                        "Resize",
                                        {
                                            "width": 736,
                                            "height": 736
                                        }
                                    ]
                                ],
                                "only_resize": True,
                                "keep_ratio": True
                            },
                            {
                                "class": "data.processes.MakeICDARData"
                            },
                            {
                                "class": "data.processes.MakeSegDetectionData"
                            },
                            {
                                "class": "data.processes.NormalizeImage"
                            }
                        ]
                    },
                    "batch_size": 1,
                    "num_workers": 16,
                    "collect_fn": {
                        "class": "data.processes.ICDARCollectFN"
                    }
                }
            },
            "visualize": False,
            "interval": 4500,
            "exempt": 1
        },
        "cmd": {
            "exp": "experiments/seg_detector/td500_resnet18_deform_thre.yaml",
            "verbose": False,
            "visualize": False,
            "force_reload": False,
            "validate": False,
            "print_config_only": False,
            "debug": False,
            "benchmark": True,
            "distributed": False,
            "local_rank": 0,
            "num_gpus": 1
        }
    }

    # import importlib
    # cls = experiment_args.copy().pop('class')
    # package, cls = cls.rsplit('.', 1)
    # module = importlib.import_module(package)
    # cls = getattr(module, cls)
    # experiment = cls(**experiment_args)

    from experiment import Experiment
    experiment = Experiment(**experiment_args)

    experiment = Configurable.construct_class_from_config(experiment_args)

    if not args['print_config_only']:
        torch.backends.cudnn.benchmark = args['benchmark']
        trainer = Trainer(experiment)
        trainer.train()


if __name__ == '__main__':
    main()
