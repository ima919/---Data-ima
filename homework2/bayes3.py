# -*- coding: utf-8 -*-
from os import listdir,mkdir,path
import random

#划分训练集和测试集,按照训练集：测试集=8：2的比例划分
def divide(index,classed, Percent):
    f3 = open(classed, 'w')
    filedir = 'data_make'#预处理之后的数据
    FilesList = listdir(filedir)
    for i in range(len(FilesList)):
        dataDir = filedir + '/' + FilesList[i]
        dataList = listdir(dataDir)
        m = len(dataList)
        test0= index*(m * (1 - Percent))#自定义划分测试集的起始位置
        test1 = (index+1)*(m * (1 - Percent))#划分测试集的结束、位置
        print(test0)
        print(test1)
        for j in range(m):
            if (j > test0) and (j < test1):#将在范围内的写进测试文档所在文件夹
                f3.write('%s %s\n' % (dataList[j], FilesList[i]))
                topath = 'Test/'+FilesList[i]
            else:
                topath= 'Train/'+FilesList[i]#将剩余文档写进训练文档所在文件夹
            if path.exists(topath) == False:
                mkdir(topath)
            datapath = dataDir + '/' + dataList[j]
            data=open(datapath,'r',errors='ignore')
            data_c=data.readlines()
            ff = open(topath + '/' + dataList[j], 'w')
            for line in data_c:
                ff.write('%s\n' % line.strip('\n'))
            ff.close()
    f3.close()

def test():
    classed = 'classed.txt'
    i=random.randint(0,5)
    divide(i,classed,0.8)
    print('划分完毕')
test()