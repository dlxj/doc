#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File    : VGG-16.py
# @Time    : 2018/12/24
# @Author  : spxcds (spxcds@gmail.com)

import logging
import os
import shutil
import sys
import time

import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import tensorflow as tf
from sklearn.metrics import confusion_matrix
from tensorflow.examples.tutorials.mnist import input_data

import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding('utf-8')
plt.switch_backend('agg')
plt.style.use('ggplot')
os.environ['CUDA_VISIBLE_DEVICES'] = '1'


def hello_info():
    print('python.version: {}'.format(str(sys.version_info.major) + '.' + str(sys.version_info.minor)))
    print('tf.version: {}'.format(tf.__version__))
    print('sklearn.version: {}'.format(sklearn.__version__))
    print('numpy.version: {}'.format(np.__version__))
    print('pandas.version: {}'.format(pd.__version__))


mnist = input_data.read_data_sets('mnist_dataset/', one_hot=True)


class VGG_16(object):
    def __init__(self, learning_rate=1e-3, l2_lambda=5e-4):
        self.learning_rate = learning_rate
        self.l2_lambda = l2_lambda

        self.sess = None
        self.loss = None
        self.p = None
        self.X = None
        self.y = None
        self.one_gd_step = None

        self.train_history = []
        self.construct()

    def __del__(self):
        if self.sess:
            self.sess.close()

    def conv(self, input_tensor, name, kh, kw, dh, dw, n_output):
        """
        卷积操作

        参数
        ----------
        input_tensor: tf Tensor
        name: 卷积层名称
        kh: 卷积核高
        kw: 卷积核宽
        dh: 步幅高度
        dw: 步幅宽度
        n_output: 输出size

        返回值
        ----------
        激活层
        """
        n_input = input_tensor.get_shape()[-1].value

        kernel = tf.get_variable(
            name=name + 'kernel',
            shape=[kh, kw, n_input, n_output],
            dtype=tf.float32,
            initializer=tf.truncated_normal_initializer(stddev=0.05))
        bias = tf.get_variable(
            name=name + 'bias', shape=[n_output], dtype=tf.float32, initializer=tf.constant_initializer(0.0))

        c = tf.nn.conv2d(input_tensor, kernel, (1, dh, dw, 1), padding='SAME')
        return tf.nn.relu(tf.nn.bias_add(c, bias), name=name)

    def max_pool(self, input_tensor, name, kh, kw, dh, dw):
        """
        最大池化操作

        参数
        ----------
        input_tensor: tf Tensor
        name: 名称
        kh: 窗口高度
        kw: 窗口宽度
        dh: 步幅高度
        dw: 步幅宽度

        返回值
        ----------
        Tensor
        """

        return tf.nn.max_pool(input_tensor, ksize=[1, kh, kw, 1], strides=[1, dh, dw, 1], padding='SAME', name=name)

    def fc(self, input_tensor, name, n_output):
        """
        全连接操作

        参数
        ----------
        input_tensor: tf Tensor
        name: 名称
        n_output: 输出size

        返回值
        ----------
        激活层
        """

        n_input = input_tensor.get_shape()[-1].value
        weights = tf.get_variable(
            name=name + 'weights',
            shape=[n_input, n_output],
            dtype=tf.float32,
            initializer=tf.truncated_normal_initializer(stddev=0.05))
        tf.add_to_collection('losses', tf.nn.l2_loss(weights))
        bias = tf.get_variable(
            name=name + 'bias', shape=[n_output], dtype=tf.float32, initializer=tf.constant_initializer(0.0))

        return tf.nn.bias_add(tf.matmul(input_tensor, weights), bias)

    def construct(self):
        self.X = tf.placeholder(tf.float32, [None, 784])
        self.y = tf.placeholder(tf.float32, [None, 10])

        X = tf.reshape(self.X, [-1, 28, 28, 1])

        # 卷积层组1 输入shape 224*224*3, 输出shape 224*224*64
        conv_1_1 = self.conv(X, 'conv_1_1', 3, 3, 1, 1, 64)
        conv_1_2 = self.conv(conv_1_1, 'conv_1_2', 3, 3, 1, 1, 64)

        # 最大值池化操作 输出 112*112*64
        pool_1 = self.max_pool(conv_1_2, 'pool_1', 2, 2, 2, 2)

        # 卷积层组2 输出 112*112*128
        conv_2_1 = self.conv(pool_1, 'conv_2_1', 3, 3, 1, 1, 128)
        conv_2_2 = self.conv(conv_2_1, 'conv_2_2', 3, 3, 1, 1, 128)

        # 最大值池化操作 输出 56*56*128
        pool_2 = self.max_pool(conv_2_2, 'pool_2', 2, 2, 2, 2)

        # 卷积层组3 输出 56*56*256
        conv_3_1 = self.conv(pool_2, 'conv_3_1', 3, 3, 1, 1, 256)
        conv_3_2 = self.conv(conv_3_1, 'conv_3_2', 3, 3, 1, 1, 256)
        conv_3_3 = self.conv(conv_3_2, 'conv_3_3', 3, 3, 1, 1, 256)

        # 最大值池化操作, 输出 28*28*256
        pool_3 = self.max_pool(conv_3_3, 'pool_3', 2, 2, 2, 2)

        # 卷积层组4 输出 28*28*512
        conv_4_1 = self.conv(pool_3, 'conv_4_1', 3, 3, 1, 1, 512)
        conv_4_2 = self.conv(conv_4_1, 'conv_4_2', 3, 3, 1, 1, 512)
        conv_4_3 = self.conv(conv_4_2, 'conv_4_3', 3, 3, 1, 1, 512)

        # 最大值池化操作 输出 14*14*512
        pool_4 = self.max_pool(conv_4_3, 'pool_4', 2, 2, 2, 2)

        # 卷积层组5 输出 14*14*512
        conv_5_1 = self.conv(pool_4, 'conv_5_1', 3, 3, 1, 1, 512)
        conv_5_2 = self.conv(conv_5_1, 'conv_5_2', 3, 3, 1, 1, 512)
        conv_5_3 = self.conv(conv_5_2, 'conv_5_3', 3, 3, 1, 1, 512)

        # 最大值池化操作 输出 7*7*512
        pool_5 = self.max_pool(conv_5_3, 'pool_5', 2, 2, 2, 2)

        shape_size = 1
        for i in range(1, 4):
            shape_size = shape_size * pool_5.get_shape()[-i].value
        reshaped = tf.reshape(pool_5, [-1, shape_size], name='reshaped')

        # 全连接层 输出 10
        fc_6 = self.fc(reshaped, 'fc_6', 128)
        relu_fc_6 = tf.nn.relu(fc_6)

        fc_7 = self.fc(relu_fc_6, 'fc_7', 128)
        relu_fc_7 = tf.nn.relu(fc_7)

        fc_8 = self.fc(relu_fc_7, 'fc_8', 10)

        self.p = tf.nn.softmax(fc_8)

        # 定义交叉熵损失函数
        cost_cross_entropy = tf.reduce_mean(
            -tf.reduce_sum(self.y * tf.log(tf.clip_by_value(self.p, 1e-10, 1.0)), axis=1))

        self.loss = tf.add(cost_cross_entropy, self.l2_lambda * tf.add_n(tf.get_collection('losses')))

        optimizer = tf.train.AdamOptimizer(self.learning_rate)
        self.one_gd_step = optimizer.minimize(self.loss)

        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.7)
        self.sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    def fit(self, epoch=10, batch_size=50):
        sess = self.sess
        sess.run(tf.global_variables_initializer())

        iterations = 0

        for i in range(epoch):
            number_batch = int(mnist.train.num_examples / batch_size)
            for j in range(number_batch):
                iterations += 1
                train_x, train_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([self.one_gd_step, self.loss], feed_dict={self.X: train_x, self.y: train_y})

                if iterations % 100 == 0:
                    self.add_record(iterations, train_x, train_y, mnist.test.images, mnist.test.labels)

    def get_loss(self, data_x, data_y):
        return self.sess.run(self.loss, feed_dict={self.X: data_x, self.y: data_y})

    def predict(self, data_x):
        pred_values = tf.argmax(self.p, 1)
        return self.sess.run(pred_values, feed_dict={self.X: data_x})

    def get_accuracy(self, data_x, data_y):
        correct_prediction = tf.equal(tf.argmax(self.p, 1), tf.argmax(self.y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        return self.sess.run(accuracy, feed_dict={self.X: data_x, self.y: data_y})

    def get_confusion_matrix(self, data_x, data_y):
        y_pred = self.predict(data_x=data_x)
        y_true = data_y.argmax(axis=1)
        return confusion_matrix(y_true=y_true, y_pred=y_pred, labels=np.arange(10)).tolist()

    def add_record(self, iterations, train_x, train_y, val_x, val_y):
        train_acc = self.get_accuracy(train_x, train_y)
        train_loss = self.get_loss(train_x, train_y)

        val_acc = self.get_accuracy(val_x, val_y)
        val_loss = self.get_loss(val_x, val_y)
        print('iterations: {} train_acc: {:.6} val_acc: {:.6} train_loss: {:.6} val_loss: {:.6}'.format(
            iterations, train_acc, val_acc, train_loss, val_loss))
        self.train_history.append([iterations, train_acc, val_acc, train_loss, val_loss])

    def plot(self, save_path):
        df = pd.DataFrame(self.train_history, columns=['iterations', 'train_acc', 'val_acc', 'train_loss', 'val_loss'])

        # loss
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(121)
        ax.grid(True)
        ax.plot(df.iterations, df.train_loss, 'k', label='训练集损失', linewidth=1.2, alpha=0.4)
        ax.plot(df.iterations, df.val_loss, 'k--', label='验证集损失', linewidth=2)
        ax.legend(fontsize=16)
        ax.set_xlabel('Iterations', fontsize=16)
        ax.set_ylabel('Loss', fontsize=16)
        ax.set_xlim(np.min(df.iterations), np.max(df.iterations) + 0.1, auto=True)
        ax.tick_params(axis='both', which='major')
        ax.set_title('损失曲线', fontsize=22)

        # accuracy
        ax = fig.add_subplot(122)
        ax.grid(True)
        ax.plot(df.iterations, df.train_acc, 'k', label='训练集正确率', linewidth=1.2, alpha=0.4)
        ax.plot(df.iterations, df.val_acc, 'k--', label='测试集正确率', linewidth=2)
        ax.legend(fontsize=16)
        ax.set_xlabel("Iterations", fontsize=16)
        ax.set_ylabel("Accuracy", fontsize=16)
        ax.tick_params(axis='both', which='major')
        ax.set_xlim(np.min(df.iterations), np.max(df.iterations) + 0.1)
        ax.set_ylim(0.0, 1.0)
        ax.set_title('正确率曲线', fontsize=22)
        plt.savefig(save_path + '_loss_600.png', format='png', dpi=600)
        plt.savefig(save_path + '_loss_1200.png', format='png', dpi=1200)

        fig_matrix_confusion = plt.figure(figsize=(10, 10))
        ax = fig_matrix_confusion.add_subplot(111)
        confusion_matrix = self.get_confusion_matrix(mnist.test.images, mnist.test.labels)
        sns.heatmap(
            confusion_matrix,
            fmt='',
            cmap=plt.cm.Greys,
            square=True,
            cbar=False,
            ax=ax,
            annot=True,
            xticklabels=np.arange(10),
            yticklabels=np.arange(10),
            annot_kws={'fontsize': 20})
        ax.set_xlabel('Predicted', fontsize=16)
        ax.set_ylabel('True', fontsize=16)
        ax.tick_params(labelsize=14)
        ax.set_title('混淆矩阵', fontsize=22)
        plt.savefig(save_path + '_confusion_matrix_600.png', format='png', dpi=600)
        plt.savefig(save_path + '_confusion_matrix_1200.png', format='png', dpi=1200)
        plt.close()

    def save(self, save_path):
        saver = tf.train.Saver()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_path = os.path.join(save_path, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())))
        saver.save(self.sess, save_path)


def main():
    vgg = VGG_16()
    vgg.fit(epoch=10, batch_size=64)
    vgg.save('VGG_16_model')
    vgg.plot('VGG_16')


if __name__ == '__main__':
    main()
