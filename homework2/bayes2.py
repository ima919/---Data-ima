# -*- coding: utf-8 -*-
from os import listdir

#统计词频(由于数据量过大，只统计词频大于4的单词）
def count():
    allword = {}
    newallword = {}
    filedir = 'data_make'#已经预处理过的文档
    fileslist = listdir(filedir)
    for i in range(len(fileslist)):
        datadir = filedir + '/' + fileslist[i]
        datalist = listdir(datadir)
        for j in range(len(datalist)):
            dadir = datadir + '/' + datalist[j]
            for line in open(dadir).readlines():
                word = line.strip('\n')
                allword[word] = allword.get(word,0.0) + 1.0
    for key, value in allword.items():#筛选
        if value > 4:
            newallword[key] = value
    sortednew = sorted(newallword.items())#排序
    print('统计词频完毕')
    return sortednew

##建立字典
def print_allword():
    f2 = open('allword.txt','w')#allowed为筛选过后的字典
    sortedallword = count()
    for item in sortedallword:
        f2.write('%s %.1f\n' % (item[0],item[1]))
    print('建立字典完毕')

print_allword()