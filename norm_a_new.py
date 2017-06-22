import numpy as np
import random
from scipy.stats import norm
from scipy.stats import dirichlet
import argparse
import matplotlib.pyplot as plt

#パサー作成
parser = argparse.ArgumentParser()
parser.add_argument("--data",type=int)
parser.add_argument("--categorical",type=int)
#parser.add_argument("--data",type=int)



#引数を作成
args = parser.parse_args()


def dirchlet_function(alpha):
    """
    引数alphaはディリクレ分布のパラメータ
    パラメータに従ってディリクレ分布を作成し，そこから値を生成する
    """
    #ディリクレ分布を作成
    seed = np.random.dirichlet(alpha)
    print("#######ディリクレ分布から値を生成####")
    print(seed)
    return seed

def categorical(n,array):
    """
    n:カテゴリ数
    array:引数としての配列，ディリクレ分布に従う（確率の和は0)
    size：次元
    return :カテゴリ分けした配列
    """
    b = np.random.multinomial(n,array)
    print("####カテゴリ分布から値を生成####")
    print(array)
    print(b)
    return b

#カテゴリ分布
# def topics(seed):
#     # print("カテゴリ分布")
#     # print(seed)
#     # print(seed.shape)
#     # for i in range(len(seed)):
#     #     print(i)
#
#     print("カテゴリ分布に従って生成したパラメータ")
#     for x in range(len(seed)):
#         ###スポーツ，経済，政治の三つのトピックを選ぶ###
#         if 0 <= x < 0.2:
#             print("1")
#             #return 1 #スポーツ
#         elif 0.2 <= x < 0.7:
#             print("2")
#             #return 2 #経済
#         elif 0.7<= x <=1:
#             print("3")
#             #return 3 #政治
#         else :
#             print("error")
#             #return "error"


def gauss(z):
    """
    ガウス分布，引数z:配列
    与えられた配列から平均，標準偏差を求めてガウス分布を作成する
    """
    #値の初期化
    average = np.mean(z)
    sigma = np.var(z)
    sd = np.std(z)
    p = norm.pdf(z,average,sd)

    # 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
    print("#######ガウス分布##########")
    print("平均",average, "標準偏差",sd,"のガウス分布が生成された")
    print("x = ",random.choice(p))
    #print("p",p)

    #print(max(p),min(p))
    n = np.arange(min(p),max(p),0.01)
    #平均0, 標準偏差10の正規分布における、xの確率を求める
    temp = []
    for i in range(len(n)):
        temp.append(norm.pdf(x=n[i], loc=average, scale=sd))

    #print(p)
    plt.scatter(n, temp)
    plt.xlim(-2,2)
    #plt.xrange(-1,1)

    plt.show()
    #print(p)
    return p



# a = np.arange(-1,1,0.1)
#
# gauss(a)

alpha_seed = args.data
alpha = [alpha_seed]*5
categorical_number = args.categorical

print("----------------------------------")
print("初期値α:",alpha)
print("カテゴリ数:",categorical_number)
print("\n")



b = dirchlet_function(alpha)
#カテゴリ数もコマンドライン引数から
z = categorical(categorical_number,b)
gauss(z)
print("----------------------------------")

# topics(b)
# # print(topics(b))
