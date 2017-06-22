# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random
import argparse

#パサー作成
parser = argparse.ArgumentParser()
parser.add_argument("--data",type=float)

#引数を作る
args = parser.parse_args()

#パラメータ
theta = args.data

print("theta:",theta)


def topics(x):
    """
    トピックを決定する．
    確率：トピック
    -------------
    0.2 : 1
    0.5 : 2
    0.3 : 3
    """
    if 0 <= x < 0.2:
        return 1 #スポーツ
    elif 0.2 <= x < 0.7:
        return 2 #経済
    elif 0.7<= x <= 1:
        return 3 #政治
    else :
        return "error"


print("カテゴリ分布の種類:",topics(theta))


if topics(theta) == 1:
    # ベクトルxを [-5.0, ..., 5.0] の区間で作成
    n = np.linspace(-5.0, 5.0, 10000)

    # 平均0, 標準偏差1の正規分布における、xの確率を求める
    p = []
    for i in range(len(n)):
        p.append(norm.pdf(x=n[i], loc=0, scale=1))

    # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
    plt.scatter(n, p)
    print("平均0, 標準偏差1の正規分布からサンプリング")
    print(random.choice(p))
    plt.show()
elif topics(theta) == 2:
    # ベクトルxを [-5.0, ..., 5.0] の区間で作成
    n = np.linspace(-5.0, 5.0, 10000)

    # 平均0, 標準偏差10の正規分布における、xの確率を求める
    p = []
    for i in range(len(n)):
        p.append(norm.pdf(x=n[i], loc=0, scale=2))

    # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
    plt.scatter(n, p)
    print("平均0, 標準偏差2の正規分布からサンプリング")
    print(random.choice(p))

    plt.show()

elif topics(theta) == 3:
    # ベクトルxを [-5.0, ..., 5.0] の区間で作成
    n = np.linspace(-5.0, 5.0, 10000)

    # 平均1, 標準偏差2の正規分布における、xの確率を求める
    p = []
    for i in range(len(n)):
        p.append(norm.pdf(x=n[i], loc=1, scale=2))

    # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
    plt.scatter(n, p)
    print("平均1, 標準偏差2の正規分布からサンプリング")
    print(random.choice(p))

    plt.show()



#ここまでで，nとpにガウス分布が格納されている
"""
    カテゴリ1 : "平均0, 標準偏差1の正規分布からサンプリング"
    カテゴリ2 : "平均0, 標準偏差2の正規分布からサンプリング"
    カテゴリ3 : "平均1, 標準偏差2の正規分布からサンプリング"
"""

for i in range(n):
