#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'

import numpy
import operator
import os
from Simple_kNN import classify0


def img2vector(filename):
    """
    Desc：
        将图像数据转换为向量
    Args：
        filename -- 图片文件 因为我们的输入数据的图片格式是 32 * 32的
    Returns:
        returnVect -- 图片文件处理完成后的一维矩阵
    该函数将图像转换为向量：该函数创建 1 * 1024 的NumPy数组，然后打开给定的文件，
    循环读出文件的前32行，并将每行的头32个字符值存储在NumPy数组中，最后返回数组。
    """
    returnVect = numpy.zeros((1, 1024))
    fr = open(filename, 'r')
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    """
    Desc:
        手写数字识别分类器，并将分类错误数和分类错误率打印出来
    Args:
        None
    Returns:
        None
    """
    # 1. 导入数据
    hwLabels = []
    trainingFileList = os.listdir("digits/trainingDigits") # load the training set
    m = len(trainingFileList)
    trainingMat = numpy.zeros((m, 1024))
    # hwLabels存储0～9对应的index位置， trainingMat存放的每个位置对应的图片向量
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        # 将 32*32的矩阵->1*1024的矩阵
        trainingMat[i] = img2vector('digits/trainingDigits/%s' % fileNameStr)

    # 2. 导入测试数据
    testFileList = os.listdir('digits/testDigits')  # iterate through the test set
    errorCount = 0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("分类器带回的分类: %d, 真实的分类: %d" % (classifierResult, classNumStr))
        errorCount += classifierResult != classNumStr
    print("\n错误的总数: %d" % errorCount)
    print("\n总错误率: %f" % (errorCount / mTest))

