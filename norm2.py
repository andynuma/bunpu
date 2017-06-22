# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random
import argparse
from scipy.stats import dirichlet

#パサー作成
parser = argparse.ArgumentParser()

parser.add_argument("--data",type=int)

#引数を作る
args = parser.parse_args()


#全ての元
#seed = np.random.randint(100)
# seed_list = np.random.dirichlet([1] * 100)
# seed = random.choice(seed_list)
# seed = dirichlet.pdf(x=(0.333, 0.333, 0.334), alpha=(11,11,11))
alpha = [1,2,3,4,5,6,7,8]
seed = np.random.dirichlet(alpha)

print(seed)
########カテゴリ分布（文書のトピック）##########
def topics(x):
    ###スポーツ，経済，政治の三つのトピックを選ぶ###
    if 0 <= x < 20:
        return 1 #スポーツ
    elif 20 <= x < 70:
        return 2 #経済
    elif 70<= x <=100:
        return 3 #政治
    else :
        return "error"


print("カテゴリ分布のパラメータ:",topics(seed))



if topics(seed) == 1:
    # ベクトルxを [-5.0, ..., 5.0] の区間で作成
    n = np.linspace(-5.0, 5.0, 10000)

    # 平均0, 標準偏差1の正規分布における、xの確率を求める
    p = []
    for i in range(len(n)):
        p.append(norm.pdf(x=n[i], loc=0, scale=1))

    # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
    plt.scatter(n, p)
    print("平均0, 標準偏差1の正規分布からサンプリング↓")
    print(random.choice(p))
    plt.show()
elif topics(seed) == 2:
    # ベクトルxを [-5.0, ..., 5.0] の区間で作成
    n = np.linspace(-5.0, 5.0, 10000)

    # 平均0, 標準偏差10の正規分布における、xの確率を求める
    p = []
    for i in range(len(n)):
        p.append(norm.pdf(x=n[i], loc=0, scale=10))

    # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
    plt.scatter(n, p)
    print("平均0, 標準偏差10の正規分布からサンプリング\n↓")
    print(random.choice(p))

    plt.show()

elif topics(seed) == 3:
    # ベクトルxを [-5.0, ..., 5.0] の区間で作成
    n = np.linspace(-5.0, 5.0, 10000)

    # 平均1, 標準偏差2の正規分布における、xの確率を求める
    p = []
    for i in range(len(n)):
        p.append(norm.pdf(x=n[i], loc=1, scale=2))

    # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
    plt.scatter(n, p)
    print("平均1, 標準偏差2の正規分布からサンプリング↓")
    print(random.choice(p))

    plt.show()

##############トピックごとの単語集###############
# def word(num):
#     if 0 <= num < 20:
#         return "サッカー" #スポーツ
#     elif 20 <= num < 70:
#         return "為替" #経済
#     elif 70<= num <=100:
#         return "安倍" #政治
#     else :
#         return "error"

############Pz(x)##########################################
# ベクトルxを [-5.0, ..., 5.0] の区間で作成
# n = np.linspace(-5.0, 5.0, 10000)
#
# # 平均0, 標準偏差1の正規分布における、xの確率を求める
# p = []
# for i in range(len(n)):
#     p.append(norm.pdf(x=n[i], loc=0, scale=1))
#
# # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
# plt.scatter(n, p)
# plt.show()
#
# ########################################################
