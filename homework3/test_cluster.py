from sklearn.cluster import KMeans,AffinityPropagation,MeanShift,SpectralClustering,DBSCAN,AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.feature_extraction.text import TfidfVectorizer  # 转换成tf-idf特征的矩阵
from nltk.tokenize import word_tokenize

# K-means算法
def kmeans_create(x,y,k):
    km = KMeans(n_clusters=k)
    result_kmeans = km.fit_predict(x)
    print('K-means的准确率:', normalized_mutual_info_score(result_kmeans, y))

# AffinityPropagation算法
def create_AffinityPropagation(x,y,k):
    ap = AffinityPropagation(damping=0.55, max_iter=575, convergence_iter=575, copy=True, preference=None,
                             affinity='euclidean', verbose=False)
    result_ap = ap.fit_predict(x)
    print('AffinityPropagation算法的准确率:', normalized_mutual_info_score(result_ap, y))

# meanshift算法
def meanshift_create(x, y, k):
    ms = MeanShift(bandwidth=0.65, bin_seeding=True)
    result_ms = ms.fit_predict(x)
    print('meanshift算法的准确率:', normalized_mutual_info_score(result_ms, y))

# SpectralClustering算法
def SpectralClustering_create(x, y, k):
    sc = SpectralClustering(n_clusters=k, affinity='nearest_neighbors', n_neighbors=4, eigen_solver='arpack', n_jobs=1)
    result_sc = sc.fit_predict(x)
    print('SpectralClustering算法的准确率:', normalized_mutual_info_score(result_sc, y))

#Ward hierarchical clustering算法
def hierarchicalWard(x,y,k):
    ac = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
    result_ac = ac.fit_predict(x)
    print('Ward hierarchical clustering算法的准确率:', normalized_mutual_info_score(result_ac, y))

# DBSCAN算法
def DBSCAN_create(x, y, k):
    db = DBSCAN(eps=0.7, min_samples=1)
    result_db = db.fit_predict(x)
    print('DBSCAN算法的准确率:', normalized_mutual_info_score(result_db, y))

# AgglomerativeClustering算法
def AgglomerativeClustering_create(x, y, k):
    ac = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='average')
    result_ac = ac.fit_predict(x)
    print('AgglomerativeClustering算法的准确率:', normalized_mutual_info_score(result_ac, y))

# GaussianMixture算法
def GaussianMixture_craete(x, y, k):
    gm = GaussianMixture(n_components=k, covariance_type='diag', max_iter=20, random_state=0)
    gm.fit(x)
    result_gm = gm.predict(x)
    print('GaussianMixture算法的准确率:', normalized_mutual_info_score(result_gm, y))

if __name__ == "__main__":
    text_list=[]
    cluster_list=[]
    vector_data=[]
    #count=0
    for line in open('Tweets.txt', 'r').readlines():
        dic = eval(line)
        text_list.append(dic["text"])
        cluster_list.append(dic["cluster"])
        #count +=1
    #print('cluster:')
    #print(count)
    #print(cluster_list)
    vectorizer = TfidfVectorizer(tokenizer=word_tokenize, stop_words='english')  # 初始化TfidfVectorizer
    vector_data= vectorizer.fit_transform(text_list).toarray() # 得到tf-idf矩阵，并转化成密集矩阵
    k=99
    #kmeans_create(vector_data,cluster_list,k)
    #meanshift_create(vector_data,cluster_list,k)
    #create_AffinityPropagation(vector_data,cluster_list,k)
    #DBSCAN_create(vector_data,cluster_list,k)
    #SpectralClustering_create(vector_data,cluster_list,k)
    #GaussianMixture_craete(vector_data,cluster_list,k)
    #AgglomerativeClustering_create(vector_data,cluster_list,k)
    hierarchicalWard(vector_data,cluster_list,k)


