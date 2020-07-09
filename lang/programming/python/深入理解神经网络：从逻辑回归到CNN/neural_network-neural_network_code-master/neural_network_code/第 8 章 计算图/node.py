# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:23:01 2019

@author: zhangjuefei
"""

import numpy as np

from graph import Graph, default_graph


class Node:
    """
    计算图节点类基类
    """

    def __init__(self, *parents):
        self.parents = parents  # 父节点列表
        self.children = []  # 子节点列表
        self.value = None  # 本节点的值
        self.jacobi = None  # 结果节点对本节点的雅可比矩阵
        self.graph = default_graph  # 计算图对象，默认为全局对象default_graph

        # 将本节点添加到父节点的子节点列表中
        for parent in self.parents:
            parent.children.append(self)

        # 将本节点添加到计算图中
        self.graph.add_node(self)

    def set_graph(self, graph):
        """
        设置计算图
        """
        assert isinstance(graph, Graph)
        self.graph = graph

    def get_parents(self):
        """
        获取本节点的父节点
        """
        return self.parents

    def get_children(self):
        """
        获取本节点的子节点
        """
        return self.children

    def forward(self):
        """
        前向传播计算本节点的值，若父节点的值未被计算，则递归调用父节点的forward方法
        """
        for node in self.parents:
            if node.value is None:
                node.forward()

        self.compute()

    def compute(self):
        """
        抽象方法，根据父节点的值计算本节点的值
        """
        pass

    def get_jacobi(self, parent):
        """
        抽象方法，计算本节点对某个父节点的雅可比矩阵
        """
        pass

    def backward(self, result):
        """
        反向传播，计算结果节点对本节点的雅可比矩阵
        """
        if self.jacobi is None:
            if self is result:
                self.jacobi = np.mat(np.eye(self.dimension()))
            else:
                self.jacobi = np.mat(np.zeros((result.dimension(), self.dimension())))

                for child in self.get_children():
                    if child.value is not None:
                        self.jacobi += child.backward(result) * child.get_jacobi(self)

        return self.jacobi

    def clear_jacobi(self):
        """
        清空结果节点对本节点的雅可比矩阵
        """
        self.jacobi = None

    def dimension(self):
        """
        返回本节点的值的向量维数
        """
        return self.value.shape[0] if self.value is not None else None

    def reset_value(self, recursive=True):
        """
        重置本节点的值，并递归重置本节点的下游节点的值
        """

        self.value = None

        if recursive:
            for child in self.children:
                child.reset_value()


class Variable(Node):
    """
    变（向）量节点
    """

    def __init__(self, dim, init=False, trainable=True):
        """
        变量节点没有父节点，构造函数接受变量的维数，以及变量是否参与训练的标识
        """
        Node.__init__(self)
        self.dim = dim

        # 如果需要初始化，则以正态分布随机初始化变量的值
        if init:
            self.value = np.mat(np.random.normal(0, 0.001, (self.dim, 1)))

        # 变量节点是否参与训练
        self.trainable = trainable

    def set_value(self, value):
        """
        为变量赋值
        """
        assert isinstance(value, np.matrix) and value.shape == (self.dim, 1)

        # 本节点的值被改变，重置所有下游节点的值
        self.reset_value()
        self.value = value


class Add(Node):
    """
    向量加法
    """

    def compute(self):
        assert len(self.parents) == 2 and self.parents[0].dimension() == self.parents[1].dimension()
        self.value = self.parents[0].value + self.parents[1].value

    def get_jacobi(self, parent):
        return np.mat(np.eye(self.dimension()))  # 向量之和对其中任一个向量的雅可比矩阵是单位矩阵


class Dot(Node):
    """
    向量内积
    """

    def compute(self):
        assert len(self.parents) == 2 and self.parents[0].dimension() == self.parents[1].dimension()
        self.value = self.parents[0].value.T * self.parents[1].value  # 1x1矩阵（标量），为两个父节点的内积

    def get_jacobi(self, parent):
        if parent is self.parents[0]:
            return self.parents[1].value.T
        else:
            return self.parents[0].value.T


class Logistic(Node):
    """
    对向量的分量施加Logistic函数
    """

    def compute(self):
        x = self.parents[0].value
        self.value = np.mat(1.0 / (1.0 + np.power(np.e, np.where(-x > 1e2, 1e2, -x))))  # 对父节点的每个分量施加Logistic

    def get_jacobi(self, parent):
        return np.diag(np.mat(np.multiply(self.value, 1 - self.value)).A1)


class ReLU(Node):
    """
    对向量的分量施加ReLU函数
    """

    def compute(self):
        self.value = np.mat(np.where(self.parents[0].value > 0.0, self.parents[0].value, 0.1 * self.parents[0].value))  # 对父节点的每个分量施加 logistic

    def get_jacobi(self, parent):
        return np.diag(np.where(self.parents[0].value.A1 > 0.0, 1.0, 0.1))


class Vectorize(Node):
    """
    将多个父节点组装成一个向量
    """

    def compute(self):
        assert len(self.parents) > 0
        self.value = np.mat(np.array([node.value for node in self.parents])).T  # 将本节点的父节点的值列成向量

    def get_jacobi(self, parent):
        return np.mat([node is parent for node in self.parents]).astype(np.float).T


class SoftMax(Node):
    """
    SoftMax函数
    """

    @staticmethod
    def softmax(a):
        a[a > 1e2] = 1e2  # 防止指数过大
        ep = np.power(np.e, a)
        return ep / np.sum(ep)

    def compute(self):
        self.value = SoftMax.softmax(self.parents[0].value)

    def get_jacobi(self, parent):
        """
        我们不实现SoftMax节点的get_jacobi函数，训练时使用CrossEntropyWithSoftMax节点（见下）
        """
        return np.mat(np.eye(self.dimension()))  # 无用


class CrossEntropyWithSoftMax(Node):
    """
    对第一个父节点施加SoftMax之后，再以第二个父节点为标签One-Hot向量计算交叉熵
    """

    def compute(self):
        prob = SoftMax.softmax(self.parents[0].value)
        self.value = np.mat(-np.sum(np.multiply(self.parents[1].value, np.log(prob + 1e-10))))

    def get_jacobi(self, parent):
        # 这里存在重复计算，但为了代码清晰简洁，舍弃进一步优化
        prob = SoftMax.softmax(self.parents[0].value)
        if parent is self.parents[0]:
            return (prob - self.parents[1].value).T
        else:
            return (-np.log(prob)).T