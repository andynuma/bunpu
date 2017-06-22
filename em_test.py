# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random
import argparse

def gauss(x,average,sd):
    """
    平均average,分散sdのガウス分布に従って値を返す
    """
    return norm.pdf(x=x,loc = average,scale = sd)

def decision_topics(x):
    """
    トピックを決定する．
    確率：トピック
    -------------
    0.2 : 1
    0.5 : 2
    0.3 : 3
    """
    if 0 <= x < 0.5:
        return 1 #スポーツ
    elif 0.5 <= x <= 1:
        return 2 #経済
    # elif 0.7<= x <= 1:
    #     return 3 #政治
    else :
        return "error"


def create(seed,x):
    """
    トピックとガウス分布を関連付ける
    """
    topic = decision_topics(seed)
    if topic == 1:
        return gauss(x,3,1)
    elif topic == 2:
        return gauss(x,-1,0.5)
    # elif topic == 3:
    #     return gauss(x,3,1)

def sampling(x):
    """
    トピックが決定して，それに従って生成された分布fからサンプリング
    x:サンプリング値の中心
    """
    #xプラスマイナス5の値を生成
    temp = x
    x_min = x - 5
    x_max = x + 5
    n = np.linspace(x_min,x_max,1000)

    result = []
    #seed = np.random.rand(10000)
    #seed = 0.3

    #print(len(n)/2)

    for i in range(len(n)):
        #result.append(create(seed[i],n[i]))
        # while n[i] < 0.7:
        #     result.append(create(seed,n[i]))
        result.append(create(np.random.rand(),n[i]))
    return n,result



#print(create(0.1,0))
n,result = sampling(1)

plt.hist(result, bins=100, normed=True)
plt.show()
#plt.scatter(n,result)
#plt.hist(result)
#plt.show()

#resultにデータ分布が入っている

def likelihood(result,mu,sd,pi,k):
    """
    対数尤度関数
    x:データ
    mu:平均
    sd:分散
    pi:混合係数
    k:トピック数
    対数尤度を返す
    """

    temp = 0
    y = 0

    for i in range(len(result)):
        for j in range(k):
            temp += (pi[j] * gauss(i,mu[j],sd[j]))
        y += np.log(temp)
    return y

mu = [1,1]
sd = [1,1]
pi = [0.5,0.5]
# print(likelihood(result,mu,sd,pi,2))

k = 2
s = 0
gamma = np.zeros((len(result),k))

#Estep
# for n in result:
#     s = 0
#     for j in range(k):
#         #負担率の分母を計算
#         s  += pi[j] * gauss(n,mu[j],sd[j])
#         print("mu:",mu,"sd:",sd)
#     for i in range(k):
#         gamma[n][i] = pi[i] * gauss(n,mu[i],mu[i]) / s
#         print(n,i,gamma[n][i])
# print(gamma)
