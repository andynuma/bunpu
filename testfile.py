import numpy as np
import random
import argparse
from scipy.stats import norm
import matplotlib.pyplot as plt


#パサー作成
parser = argparse.ArgumentParser()

#parser.add_argument('--infile', type=argparse.FileType('r'))
parser.add_argument('--infile', type=str,nargs=1)
#引数を作る
args = parser.parse_args()


#ファイルから数字をとってくる
def file_to_data(filename):
    return np.loadtxt(filename,delimiter=",")


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
    #print("#######ガウス分布##########")
    #print("平均",average, "標準偏差",sd,"のガウス分布が生成された")
    print("サンプリング ：",random.choice(p))
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

    # plt.show()
    #print(p)
    return p


filename = args.infile[0]

b = file_to_data(filename)

# print(b)

array = file_to_data(filename)
#print(array)

def array_to_data(array,i,j):
    """
    arrayのi,j番目の要素を取ってくる関数
    """
    return array[i][j]

#before = np.random.randint(3)
after = np.random.randint(3)

#print("index : ",before,after)

#b = array_to_data(array,before,after)
print("遷移確率の行列 = ")
print(array)
current_position = 0
after = current_position
print("状態",current_position)


for i in range(4):


    #遷移先を決定
    #after = current_position + 1

    #遷移確率
    p = array_to_data(array,current_position,after)

    #0~1の乱数を生成して確率とする
    flag = np.random.rand()
    # seed_flag = np.arange(0,1,0.1)
    # #print(seed_flag)
    # num = np.random.randint(4)
    # flag = seed_flag[num]

    #print("flag:",flag,"p:",p)#"after",after,"\n")
    # print("position:",current_position)
    # print("before",current_position,"after",after)
    print("遷移確率：",p)

    #遷移するとき
    if flag < p:
        after = current_position + 1
        current_position = after
        #print("ifafter",after)
    else:
        current_position = current_position

    print("状態",current_position)

    if current_position == 0 :
        z = np.arange(np.random.randint(10)*3)
    else :
        z = np.arange(current_position*3)
    gauss(z)
    print("----------------------")

    if current_position == 0 :
        z = np.arange(np.random.randint(1,10)*3)
    else :
        z = np.arange(current_position*3)
