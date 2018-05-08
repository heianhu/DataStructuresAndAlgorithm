#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'

from numpy import *
import re
import operator
import feedparser


def loadDataSet():
    """
    准备数据:创建一些实验样本
    """
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]  # 进行词条切分后的文档集合
    # 这里有两类，侮辱性和非侮辱性，1代表辱骂的词汇，0代表不是。
    # 这些文本的类别由人工标注，这些标 注信息用于训练程序以便自动检测侮辱性留言。
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


def createVocabList(dataSet):
    """
    准备数据:创建一个包含在所有文档中出现的不重复词的列表
    :param dataSet:
    :return:
    """
    vocabSet = set([])  # 创建一个空集
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 求连个集合的并集
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    """
    准备数据:词表到向量的转换函数
    :param vocabList:词汇表
    :param inputSet:某个文档
    :return:文档向量，向量的每一元素为1或0，分别表示词汇表中的单词在输入文档中是否出现
    """
    returnVec = [0] * len(vocabList)  # 创建一个所有元素都为0的向量
    # 遍历文档中的所有单词，如果出现了词汇表中的单词，则将输出的文档向量中的对应值设为1。
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    """
    训练算法:朴素贝叶斯分类器训练函数
    :param trainMatrix:文档矩阵
    :param trainCategory:每篇文档类别标签所构成的向量
    :return:两个向量和一个概率(文档属于侮辱性0 文档(class=1)的概率)
    """
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 计算文档属于侮辱性文档(class=1)的概率
    p0Num = ones(numWords)
    p1Num = ones(numWords)  # 初始化，如果其中一个概率值为0，那么最后的乘积也为0。为降低 这种影响，可以将所有词的出现数初始化为1。
    p0Denom = 2.0
    p1Denom = 2.0  # 初始化，如果其中一个概率值为0，那么最后的乘积也为0。为降低 这种影响，可以将所有词的出现数初始化为1，并将分母初始化为2。
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)  # 因为下溢出问题(这是由于太多很小的数相乘造成的)，所以将除数取对数
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    """
    测试算法:朴素贝叶斯分类函数
    :param vec2Classify:要分类的向量
    :param p0Vec:来自于trainNB0()
    :param p1Vec:来自于trainNB0()
    :param pClass1:来自于trainNB0()
    :return:
    """
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # 元素相乘
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def bagOfWords2VecMN(vocabList, inputSet):
    """
    朴素贝叶斯词袋模型
    :param vocabList:
    :param inputSet:
    :return:
    """
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def tNB():
    """
    测试算法:该函数封装所有操作，用于测试
    :return:
    """
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))

    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))


def textParse(bigString):  # input is big string, #output is word list
    """
    文件解析(不包含少于两个字符的字符串)并将所有字符串转换为小写
    :param bigString: 一篇文章
    :return: 将文章分割为单个单词
    """
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    """
    完整的垃圾邮件测试函数
    :return:
    """
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):
        # 将文章读入
        wordList = textParse(open('email/spam/%d.txt' % i, encoding='utf-8').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i, encoding='utf-8').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)  # 创建一个词汇表
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        # 随机构建训练集
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:  # 用trainNB0()方法将数据trainingSet训练集训练
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:  # 用剩余的测试集测试
        # 对测试集分类
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print("分类错误:", docList[docIndex])
    print('出错率为: ', float(errorCount) / len(testSet))
    # return vocabList,fullText


if __name__ == '__main__':
    spamTest()
