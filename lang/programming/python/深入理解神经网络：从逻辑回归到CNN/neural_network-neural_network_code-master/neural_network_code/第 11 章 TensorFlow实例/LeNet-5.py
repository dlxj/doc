# -*- coding: utf-8 -*-

# @File    : LeNet-5.py
# @Time    : 2018/11/28
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


class LeNet_5(object):
    def __init__(self, learning_rate=5e-3, l2_lambda=8e-4):
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

        X = tf.reshape(self.X, [-1, 28, 28, 1])

        # 第一层：卷积层 输出 28*28*6
        conv1_w = tf.get_variable('conv1_w', [5, 5, 1, 6], initializer=tf.truncated_normal_initializer(stddev=0.05))
        conv1_b = tf.get_variable('conv1_b', [6], initializer=tf.constant_initializer(0.0))
        conv1 = tf.nn.conv2d(X, conv1_w, strides=[1, 1, 1, 1], padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_b))

        # 第二层：平均值池化层 输出 14*14*6
        pool2 = tf.nn.avg_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

        # 第三层：卷积层 输出 10*10*16
        conv3_w = tf.get_variable('conv3_w', [5, 5, 6, 16], initializer=tf.truncated_normal_initializer(stddev=0.05))
        conv3_b = tf.get_variable('conv3_b', [16], initializer=tf.constant_initializer(0.0))
        conv3 = tf.nn.conv2d(pool2, conv3_w, strides=[1, 1, 1, 1], padding='VALID')
        relu3 = tf.nn.relu(tf.nn.bias_add(conv3, conv3_b))

        # 第四层：平均值池化层 输出 5*5*16
        pool4 = tf.nn.avg_pool(relu3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

        # 第五层：卷积层 输出 1*1*120
        conv5_w = tf.get_variable('conv5_w', [5, 5, 16, 120], initializer=tf.truncated_normal_initializer(stddev=0.05))
        conv5_b = tf.get_variable('conv5_b', [120], initializer=tf.constant_initializer(0.0))
        conv5 = tf.nn.conv2d(pool4, conv5_w, strides=[1, 1, 1, 1], padding='VALID')
        relu5 = tf.nn.relu(tf.nn.bias_add(conv5, conv5_b))
        reshaped_relu5 = tf.reshape(relu5, [-1, 120])

        # 第六层：全连接层 输出 84
        fc6_w = tf.get_variable('fc6_w', [120, 84], initializer=tf.truncated_normal_initializer(stddev=0.05))
        tf.add_to_collection('losses', tf.nn.l2_loss(fc6_w))
        fc6_b = tf.get_variable('fc6_b', [84], initializer=tf.constant_initializer(0.0))
        fc6 = tf.nn.relu(tf.matmul(reshaped_relu5, fc6_w) + fc6_b)

        # 输出层 输出 10
        fco_w = tf.get_variable('fco_w', [84, 10], initializer=tf.truncated_normal_initializer(stddev=0.05))
        tf.add_to_collection('losses', tf.nn.l2_loss(fco_w))
        fco_b = tf.get_variable('fco_b', [10], initializer=tf.constant_initializer(0.0))
        fco = tf.matmul(fc6, fco_w) + fco_b

        self.p = tf.nn.softmax(fco)

        # 定义交叉熵损失函数
        cost_cross_entropy = tf.reduce_mean(
            -tf.reduce_sum(self.y * tf.log(tf.clip_by_value(self.p, 1e-10, 1.0)), axis=1))

        self.loss = tf.add(cost_cross_entropy, self.l2_lambda * tf.add_n(tf.get_collection('losses')))

        optimizer = tf.train.GradientDescentOptimizer(self.learning_rate)
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
    lenet = LeNet_5()
    lenet.fit(epoch=40, batch_size=64)
    lenet.save('LeNet_5_model')
    lenet.plot('LeNet_5')


if __name__ == '__main__':
    main()
