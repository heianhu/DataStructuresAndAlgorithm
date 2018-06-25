#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'

import numpy
import operator
from Simple_kNN import classify0


def file2matrix(filename):
    """
    导入训练数据
    :param filename: 数据文件路径
    :return: 数据矩阵returnMat和对应的类别classLabelVector
    """
    with open(filename, 'r') as fr:
        # 获得文件中的数据行的行数
        numberOfLines = len(fr.readlines())
        # 生成对应的空矩阵
        # 例如：zeros(2，3)就是生成一个 2*3 的矩阵，各个位置上全是 0
        returnMat = numpy.zeros((numberOfLines, 3))  # prepare matrix to return
    with open(filename, 'r') as fr:
        classLabelVector = []  # prepare labels return
        index = 0
        for line in fr.readlines():
            # str.strip([chars]) --返回移除字符串头尾指定的字符生成的新字符串
            line = line.strip()
            # 以 '\t' 切割字符串
            listFromLine = line.split('\t')
            # 每列的属性数据，即 features
            returnMat[index] = listFromLine[0: 3]
            # 每列的类别数据，就是 label 标签数据
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
    # 返回数据矩阵returnMat和对应的类别classLabelVector
    return returnMat, classLabelVector


def autoNorm(dataSet):
    """
    归一化特征值，消除属性之间量级不同导致的影响
    归一化公式：
        Y = (X-Xmin)/(Xmax-Xmin)
        其中的 min 和 max 分别是数据集中的最小特征值和最大特征值。该函数可以自动将数字特征值转化为0到1的区间。
    :param dataSet: 需要进行归一化处理的数据集
    :return:
        normDataSet -- 归一化处理后得到的数据集
        ranges -- 归一化处理的范围
        minVals -- 最小值
    """
    # 计算每种属性的最大值、最小值、范围
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # 极差
    ranges = maxVals - minVals

    normDataSet = (dataSet - minVals) / ranges
    return normDataSet, ranges, minVals


def datingClassTest():
    """
    对约会网站的测试方法，并将分类错误的数量和分类错误率打印出来
    :return:
    """
    # 设置测试数据的的一个比例（训练数据集比例=1-hoRatio）
    hoRatio = 0.1  # 测试范围,一部分测试一部分作为样本
    # 从文件中加载数据
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")  # load data setfrom file
    # 归一化数据
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # m 表示数据的行数，即矩阵的第一维
    m = normMat.shape[0]
    # 设置测试的样本数量， numTestVecs:m表示训练样本的数量
    numTestVecs = int(m * hoRatio)
    print('numTestVecs=', numTestVecs)
    errorCount = 0
    for i in range(numTestVecs):
        # 对数据测试
        classifierResult = classify0(normMat[i], normMat[numTestVecs : m], datingLabels[numTestVecs : m], 3)
        print("分类器带回的分类: %d, 真实的分类: %d" % (classifierResult, datingLabels[i]))
        errorCount += classifierResult != datingLabels[i]
    print("总错误率: %f" % (errorCount / numTestVecs))
    print(errorCount)


if __name__ == '__main__':
    # a, b = file2matrix('datingTestSet2.txt')
    # normMat, ranges, minVals = autoNorm(a)
    # print(normMat)
    # print(ranges)
    # print(minVals)
    datingClassTest()
