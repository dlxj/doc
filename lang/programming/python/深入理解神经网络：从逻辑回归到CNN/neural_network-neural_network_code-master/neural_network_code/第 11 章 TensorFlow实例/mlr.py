#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File    : mlr.py
# @Time    : 2018/11/25
# @Author  : spxcds (spxcds@gmail.com)

import os
import sys

import sklearn
import numpy as np
import pandas as pd
import time
import shutil
import logging
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from sklearn.metrics import confusion_matrix

reload(sys)
sys.setdefaultencoding('utf-8')
plt.switch_backend('agg')
plt.style.use('ggplot')
os.environ["CUDA_VISIBLE_DEVICES"] = '1'


def hello_info():
    print('python.version: {}'.format(str(sys.version_info.major) + '.' + str(sys.version_info.minor)))
    print('tf.version: {}'.format(tf.__version__))
    print('sklearn.version: {}'.format(sklearn.__version__))
    print('numpy.version: {}'.format(np.__version__))
    print('pandas.version: {}'.format(pd.__version__))


mnist = input_data.read_data_sets("mnist_dataset/", one_hot=True)


class MLR(object):
    def __init__(self, learning_rate=1e-2, l2_lambda=5e-4):
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

    def construct(self):
        self.X = tf.placeholder(tf.float32, [None, 784])
        self.y = tf.placeholder(tf.float32, [None, 10])

        W = tf.Variable(tf.truncated_normal([784, 10], stddev=0.01))
        b = tf.Variable(tf.zeros([10]))

        self.p = tf.nn.softmax(tf.matmul(self.X, W) + b)

        cost_cross_entropy = tf.reduce_mean(
            -tf.reduce_sum(self.y * tf.log(tf.clip_by_value(self.p, 1e-10, 1.0)), axis=1))
        cost_regularization_l2 = self.l2_lambda * tf.reduce_sum(tf.square(W))

        self.loss = tf.add(cost_cross_entropy, cost_regularization_l2)

        optimizer = tf.train.GradientDescentOptimizer(self.learning_rate)
        self.one_gd_step = optimizer.minimize(self.loss)

        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.7)
        self.sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    def fit(self, epoch=20, batch_size=50):
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
        plt.savefig(save_path + '_loss_1200.png', format='png', dpi=600)

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

    mlr = MLR()
    mlr.fit(epoch=30, batch_size=64)
    mlr.save('mlr_model')
    mlr.plot('mlr')


if __name__ == '__main__':
    main()
