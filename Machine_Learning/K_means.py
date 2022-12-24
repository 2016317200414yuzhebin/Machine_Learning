import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn import metrics
from sklearn.cluster import KMeans
"""
    KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300,
            tol=0.0001, precompute_distances='auto', verbose=0, 
            random_state=None, copy_x=True, n_jobs=1, algorithm='auto')
        Parameters:
             n_clusters: 聚类个数
             init:      初始化质心的方法
             n_init:    用不同的质心初始化值运行算法的次数
             max_iter:  最大迭代数
             tol:       关于收敛的参数
             precompute_distances:预计算距离
             random_state: 随机种子
             copy_x:    是否修改原始数据
             n_jobs:    计算的进程数
             algorithm:"auto", "full" or "elkan"
                         "full"就是我们传统的K-Means算法, 
                         "elkan"elkan K-Means算法。默认的
                         "auto"则会根据数据值是否是稀疏的,来决定如何选择"full"和"elkan",稠密的选 "elkan",否则就是"full"
        Attributes:
             cluster_centers_:质心坐标
             Labels_: 每个点的分类 
             inertia_:每个点到其簇的质心的距离之和。 
"""

# X为数据, y_true为标签, n_samples样本个数, centers中心点个数, cluster_std每个类别的方差, random_state随机数种子
X, y_true = make_blobs(n_samples=100, centers=4, cluster_std=0.60, random_state=0)
 
def draw(m_kmeans, X, y_pred, n_clusters):
    centers = m_kmeans.cluster_centers_
    print(centers)
    plt.title("K-Means (clusters = %d)" %n_clusters, fontsize=20)
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=50, cmap='viridis')
    #中心点（质心）用红色标出
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
    print("Calinski-Harabasz score:%lf" %metrics.calinski_harabasz_score(X, y_pred)) # 评价聚类模型的好坏
    plt.show()

m_kmeans = KMeans(n_clusters=4) # 创建分类器对象
m_kmeans.fit(X) # 用训练集拟合分类器模型
y_pred = m_kmeans.predict(X) # 用模型进行预测
draw(m_kmeans, X, y_pred, 4)