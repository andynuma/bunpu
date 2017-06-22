#!/usr/bin/python
# coding: UTF-8

import numpy as np
from scipy import stats
#import matplotlib.pyplot as plt

#ファイルから数字をとってくる
def file_to_data(filename):
    return np.loadtxt(filename,delimiter=" ")

#mainにnumpyをインポートしないため
def rang(temp):
    return np.arange(len(temp))

#確率により乱数(haba)を1つ生成
def p_rand(haba,kakuritu):
    return np.random.choice(haba,p=kakuritu)


#ディリクレ分布に従う乱数生成器
def dir(alpha):
    print("******ディリクレ分布に従う乱数生成******")
    print("パラメータalpha=",alpha)
    return np.random.dirichlet(alpha)

#カテゴリ分布に従うn個の乱数生成器
def categorical(pk,n):
    print("******カテゴリ分布による乱数生成******")
    print("theta=",pk)
    xk=np.arange(len(pk))
    custm = stats.rv_discrete(name='custm', values=(xk, pk))
    z=custm.rvs(size=n)
    return z

#ガウス分布による確率モデル生成
def gaus(z):
    print("******ガウス分布による確率モデル生成******")
    heikin=np.mean(z)
    bunsan=np.var(z)
    hensa=np.std(z)
    print("パラメータの平均：",heikin)
    print("パラメータの標準偏差：",hensa)
    pzx=[]
    for i in z:
        pzx.append(stats.norm.pdf(i,heikin,hensa))
    return pzx

#確率の配列pを用いてランダムにn個の数字（確率配列の要素数-1まで）を生成
def seisei(p,l):
    print("******確率モデルから乱数を生成******")
    temp=np.arange(len(p))
    x=np.random.choice(temp,l,p)
    return x
