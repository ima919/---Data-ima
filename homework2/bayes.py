from os import listdir,mkdir,path
import re
import nltk

#新建文件夹存储预处理之后的数据
#文件夹20news-18828存放原始数据
#文件夹data_make存放预处理之后的数据
def create():
    fromfilelist = listdir('20news-18828')
    for i in range(len(fromfilelist)):
        filedir = '20news-18828/' + fromfilelist[i]
        filelist = listdir(filedir)
        todir = 'data_make/' + fromfilelist[i]
        if path.exists(todir)==False:
            mkdir(todir)  #创建目录
        else:
            print('该目录已存在')
        for j in range(len(filelist)):
            tarfile(fromfilelist[i],filelist[j])

#将预处理之后的数据写进data_make相应的文件夹
def tarfile(fromfilename,datafilename):
    fromfiles = '20news-18828/' + fromfilename +'/'+ datafilename
    tofiles = 'data_make/' + fromfilename + '/' +datafilename
    f1= open(tofiles,'w')
    datal=open(fromfiles,'r',errors='ignore')
    datalist = datal.readlines()
    for line in datalist:
        makeline = maketxt(line) #调用maketxt函数预处理数据
        for word in makeline:
            f1.write('%s\n' % word)
    f1.close()

#预处理数据
def maketxt(line):
    stopwords = nltk.corpus.stopwords.words('english') #去停用词
    porter = nltk.PorterStemmer() #词干提取
    takeunword = re.compile('[^a-zA-Z]') #去除非字母
    makeword = [porter.stem(word.lower()) for word in takeunword.split(line) if len(word)>0 and word.lower() not in stopwords]#变小写
    return makeword
create()
