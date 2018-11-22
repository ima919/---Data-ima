'''
构建向量空间模型：
    数据预处理，分别对训练数据以及测试数据进行分词等一系列的操作，将其保存至相应的train_make和test_make中，
    在此过程中计算单词的词频并构建字典allword和allword_test。
    计算权重w=tf * idf,并将文档构建成向量，将训练文档和测试文档分别保存在文件夹向量以及向量_test中，构建成功。
主要函数介绍：
    预处理函数data_make：主要进行分词，大写变小写，词形还原，词干提取，去停用词，并统计词频
    计算函数tf_idf：主要计算tf and idf 并计算w= tf * idf
    构建向量空间模型函数vsm：将处理好的文档构建成向量
'''

import nltk
import os
import sys
import csv
import string
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from textblob import TextBlob


#读取训练数据（测试数据），进行预处理(分词，大写变小写，去停用词，词干提取，词形还原）后并计算tf
def data_make(path, path2):
	allword = []#存储字典
	list = []
	files = os.listdir(path)
	for file in files:
		file_list = os.listdir(path + "/" + file)
		for file_txt in file_list:
			data = open(path + "/" + file + "/" + file_txt, 'r', errors='ignore')
			data_c = data.readlines()
			#文档预处理
			data_c = str(data_c).replace("\\n", "")
			data_c= str(data_c).lower()
			for c in string.punctuation:
				data_c = data_c.replace(c, " ")
			wordlist = nltk.word_tokenize(data_c) #分词
			filtered = [w for w in wordlist if w not in stopwords.words('english')]#去停用词
			#词干提取 and 词形还原
			ps = PorterStemmer()
			filtered = [ps.stem(w) for w in filtered]
			wl = WordNetLemmatizer()
			filtered = [wl.lemmatize(w) for w in filtered]
			#统计词频
			coun = {}
			for w in filtered:
				if w not in allword:
					allword.append(w)
				if coun.get(w) is not None:
					coun[w] += 1
				else:
					coun[w] = 1
			for k, v in coun.items():
				coun[k] = (1 + math.log(v))
			list.append(coun)
			#写入文件
			with open(path2+"/"+file+"/"+file_txt,'w+') as f:
				for k, v in coun.items():
					f.write(k + ":" + str(v) + "\n")
				with open("./allword_test.txt", 'w+') as f:
					for i in allword:
						f.write(str(i) + "\n")
	return list


#计算w= tf * idf
def tf_idf(word,w):
    dvv = {}
    allword = []#用来更新词典
    with open("./allword_test.txt",'r') as f:
        data_c = f.readlines()
        #data_c = str(data_c).replace("\\n", "")
        data_c = TextBlob(str(data_c).replace("\\n", "").replace("'", "").replace("\\t", "").replace("\\", ""))
        data_c = data_c.words
        for i in data_c:
            count = 0
            for file in word:
                if file.get(i,0)!=0:
                    count =count +1
            dvv[i] = count

    for file in word:
        for k, v in file.items():
            if dvv.get(k,0)!= 0:
                file[k] = v*math.log(len(word)/dvv[k])#tf * idf公式
                if file[k]>=w and(k not in allword):#通过设置w的大小，来控制字典的大小
                    allword.append(k)

    with open("./allword_test.txt",'w+') as f:#更新字典
       for i in allword:
            f.write(str(i)+"\n")
    return allword,word

#构建向量空间模型，分别读取train_make 和 test_make中的数据，将其构建成向量
def vsm(path,path2,word,voc):
    count = 0
    files = os.listdir(path)
    for file in files:
        file_list = os.listdir(path + "/" + file)
        for file_txt in file_list:
            with open(path2 + "/" + file + "/" + file_txt, 'w+') as f:
                for i in voc:
                    if word[count].get(i,0) != 0:
                        f.write(i+ ":" + str(word[count][i]) + "\n")
                    else:
                        f.write(i+ ":" + "0" + "\n")
            count += 1

if __name__ == "__main__":
    #list1=data_make("./20news-bydate-train","./train_make")
    list1 = data_make("./20news-bydate-test", "./test_make")
    list2,list3=tf_idf(list1,10)
    #vsm("./train_make","./向量",list3,list2)
    vsm("./test_make", "./向量_test", list3, list2)
    print("构建成功")

