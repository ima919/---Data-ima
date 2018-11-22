'''
利用贝叶斯算法进行文档的分类
1.数据预处理bayes
    文件夹20news-18828存放原始数据
    文件夹data_make存放预处理之后的数据
2.统计词频与建立字典bayes2
    allword为字典
3.划分数据集bayes3
    将数据按照8：2的比例划分成训练集以及测试集
    Test文件夹存放测试集
    Train文件夹存放训练集
    classed.txt存储测试文档原有的类别
4.贝叶斯算法bayes4
    计算条件概率与先验概率
    计算正确率
    result.txt存储分类结果
'''
# -*- coding: utf-8 -*-
from numpy import *
from os import listdir
import math

#统计训练集中不同类别下的单词总数以及每个单词出现的次数
def wordcount(path):
    WordsNum = {}
    Wordsoccur = {}
    ddir = listdir(path)
    for i in range(len(ddir)):
        count = 0 # 记录每个每个类下的单词总数
        datapath = path + '/' + ddir[i]
        fiter = listdir(datapath)
        for j in range(len(fiter)):
            Filepath = datapath + '/' + fiter[j]
            words = open(Filepath).readlines()
            for line in words:
                count = count + 1
                word = line.strip('\n')
                keyName = ddir[i] + '_' + word
                Wordsoccur[keyName] = Wordsoccur.get(keyName,0)+1 # 记录每个每个类中每个单词的出现次数
        WordsNum[ddir[i]] = count
        print('第 %d 个类统计完毕' % (i+1))
    return Wordsoccur, WordsNum

#利用贝叶斯算法对测试集进行分类
def byeas(trainpath,testpath,result):
    f4 = open(result,'w')
    Wordsoccur, WordsNum = wordcount(trainpath)#将某个类中的单词出现次数以及该类总的单词数返回
    traincount=0.0 #计算训练集所有的单词总数
    for value in WordsNum.values():
        traincount += value
    #进行分类
    testfister = listdir(testpath)
    for i in range(len(testfister)):
        testddir = testpath  +'/'+ testfister[i]
        test = listdir(testddir)
        for j in range(len(test)):
            testwords = []
            readdir = testddir +'/' + test[j]
            lines = open(readdir).readlines()
            for line in lines:
                word = line.strip('\n')
                testwords.append(word)

            maxP = 0.0
            trainddir = listdir(trainpath)
            for k in range(len(trainddir)):
                p = c_prob(trainddir[k], testwords,WordsNum, traincount, Wordsoccur)
                if p > maxP:
                    maxP = p
                    result_best = trainddir[k]
            f4.write('%s %s\n' % (test[j],result_best))
    f4.close()

#计算条件概率与先验概率
def c_prob(trainpath,testWords,WordsNum_k,WordsNum,Wordsoccur):
    prob = 0
    wordNumInCate = WordsNum_k[trainpath]  # 类k下单词总数
    for i in range(len(testWords)):
        keyName = trainpath + '_' + testWords[i]
        if keyName in Wordsoccur:
            testword_k = Wordsoccur[keyName] # 类k下词c出现的次数
        else:
            testword_k = 0.0
        countProb =math.log((testword_k + 0.0001)*(wordNumInCate + WordsNum))
        # 计算条件概率 =类k中单词i的数目/（类k中单词总数+训练样本中所有类单词总数）
        prob = prob + countProb
    r = prob + log(wordNumInCate) - log(WordsNum)
    #计算先验概率 =（类k中单词总数）/（训练样本中所有类单词总数）
    return r

#计算正确率
def comright(rightCate, resultCate):
    right = {}
    result = {}
    rightCount = 0.0

    for line in open(rightCate).readlines():
        (sampleFile, cate) = line.strip('\n').split(' ')
        right[sampleFile] = cate

    for line in open(resultCate).readlines():
        (sampleFile, cate) = line.strip('\n').split(' ')
        result[sampleFile] = cate

    for sampleFile in right.keys():
        if (right[sampleFile] == result[sampleFile]):
            rightCount += 1.0
    print('正确的个数 : %d  分类的个数: %d' % (rightCount, len(right)))
    accuracy = rightCount / len(right)
    print('正确率: %f' % (accuracy))
    return accuracy

def class_result():
    trainpath = 'Train/'
    testpath = 'Test/'
    classifyresult = 'result.txt'
    byeas(trainpath,testpath,classifyresult)

def compute():
    accuracy = []
    rightCate = 'classed.txt'
    resultCate = 'result.txt'
    accuracy.append(comright(rightCate,resultCate))
    return accuracy

class_result()
compute()
