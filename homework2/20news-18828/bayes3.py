# -*- coding: utf-8 -*-
from numpy import *
from os import listdir,mkdir,path
import re
from nltk.corpus import stopwords
import nltk
import math

#划分训练集与测试集
def make_test(classify_right, Percent=0.8):
    fr = open(classify_right, 'w')
    filedir = 'data_make'
    fileslist = listdir(filedir)
    for i in range(len(fileslist)):
        filesdir = filedir + '/' + fileslist[i]
        datalist = listdir(filesdir)
        m = len(datalist)
        testBeginIndex = m * (1 - Percent)
        testEndIndex = m * (1 - Percent)
        for j in range(m):
            # 序号在规定区间内的作为测试样本，需要为测试样本生成类别-序号文件，最后加入分类的结果，
            # 一行对应一个文件，方便统计准确率
            if (j > testBeginIndex) and (j < testEndIndex):
                fr.write('%s %s\n' % (datalist[j], fileslist[i]))  # 写入内容：每篇文档序号 它所在的文档名称即分类
                targetDir = 'TestSample/'+fileslist[i]
            else:
                targetDir = 'TrainSample/'+fileslist[i]
            if path.exists(targetDir) == False:
                mkdir(targetDir)
            sampleDir = filesdir + '/' + datalist[j]
            data=open(sampleDir,'r',errors='ignore')
            sample=data.readlines()
            #sample = open(sampleDir).readlines()
            sampleWriter = open(targetDir + '/' + datalist[j], 'w')
            for line in sample:
                sampleWriter.write('%s\n' % line.strip('\n'))
            sampleWriter.close()
    fr.close()
# 调用以上函数生成标注集，训练和测试集合
# def test():
#     for i in range(10):
#         classifyRightCate = 'classifyRightCate' + str(i) + '.txt'
#         make_test(i, classifyRightCate)
classify_right='classify_right.txt'
make_test(classify_right)