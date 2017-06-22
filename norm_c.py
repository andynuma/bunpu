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
    print("p",p)

    print(max(p),min(p))
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

def transition(input_file,z1):
    """
    状態z1からz2に遷移する関数
    状態遷移確率によって遷移するか決定する
    """

def file_to_data(filename):
    """
    csv形式のファイルからデータを取ってくる

    """
    return np.loadtxt(filename,delimiter=",")


def array_to_data(array,i,j):
    """
    arrayのi,j番目の要素を取ってくる関数
    """
    return array[i][j]


print("----------------------------------")
# print("初期値α:",alpha)
# print("カテゴリ数:",categorical_number)
print("\n")


filename = args.infile[0]
b = dirchlet_function(alpha)
#カテゴリ数もコマンドライン引数から
z = categorical(categorical_number,b)
gauss(z)
print("----------------------------------")

# topics(b)
# # print(topics(b))
