'''
KNN：
    1.是通过测量不同特征值之间的距离进行分类。
    2.采用余弦距离的近邻度量的方法，利用多维公式计算距离。
      当两个向量的方向重合时夹角余弦取最大值1，此时两个向量的相似性最高，
      当两个向量的方向完全相反夹角余弦取最小值-1，此时两个向量的相似性为负。
    3.k值的选择：K值一般取一个比较小的数值，通常采用交叉验证法（简单来说，就是一部分样本做训练集，一部分做测试集）
      通过观察K值不同时模型的分类效果来选择最优的K值。
主演函数介绍：函数cosine用来计算余弦距离
            函数read_file用来读取训练集和测试集的向量数据
            函数knn,分类并计算正确率。设定K的值，对于测试集的每一个向量，让其与训练集里的所有向量进行比较，保留下前K个与其最相似（cos值大）的向量，
            统计出前k个中出现的最多次数的类别，让其与该向量的类别比较，若相同，即正确。
'''
import math
import os

dic_test={}
dic_train={}

##计算余弦距离,利用多项式的余弦距离公式计算
def cosine(test,train):
    x=0
    y1=0
    y2=0
    for k in range(len(train)):
        x +=train[k]*test[k]#公式中的分子
        y1 +=train[k]*train[k]#公式中的分母
        y2 +=test[k]*test[k]#公式中的分母
    if y1*y2>0:
        return x/((pow(y1,0.5)*pow(y2,0.5)))#余弦距离计算公式
    else:
        return 10000000
#读取向量
def read_file(path,w):
    files=os.listdir(path)
    for file in files:
        file_lb=os.listdir(path +"/" + file)
        for i in range(len(file_lb)):
            list=[]
            txt=path + "/" + file + "/" + file_lb[i]
            with open(txt,'r',errors='ignort') as f:
                data=f.readlines()
                for i in data:
                    temp=i.split(":")[1]
                    temp=temp.strip('\n')
                    list.append(float(temp))
                if w == 1:
                    dic_test[txt] = list#获取测试数据向量
                else:
                    dic_train[txt] =list#获取训练数据向量

#knn算法实现
def knn(dic_train,dic_test,k):
    count=0#统计总次数
    right=0#统计正确次数
    for test_key in dic_test.keys():
        distance = {}
        for train_key in dic_train.keys():
            test_vec = dic_test[test_key]
            train_vec = dic_train[train_key]
            d = cosine(test_vec, train_vec) #调用余弦函数，计算余弦距离
            distance[train_key] = d
        distance = sorted(distance.items(), key=lambda x: x[1], reverse=True)#对距离进行排序
        dic = {}
        count += 1
        for i in range(k):
            if dic.get(distance[i][0].split("/")[2]) is None:
                dic[distance[i][0].split("/")[2]] = 1
            else:
                dic[distance[i][0].split("/")[2]] += 1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        if dic[0][0] == test_key.split("/")[2]:#统计预测正确的次数
            right += 1
    print("正确率：" + str(right / count))

if __name__ == "__main__":
    read_file("./向量_test", 1)
    read_file("./向量", 2)
    knn(dic_train,dic_test,7)