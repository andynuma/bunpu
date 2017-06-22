import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import argparse

def set_param(theta):
    """
    theta : 初期値 (0~1)
    thetaによって，カテゴリを決定し，
    そのカテゴリのガウス分布の
    平均mu,標準偏差sigmaを設定する．
    return : mu , sigma

    #カテゴリ数は2
    """
    #平均と標準偏差を初期化
    mu = 0
    sigma = 0

    #カテゴリ
    categorical = 0

    #0.3の確率でカテゴリ1,0.7の確率でカテゴリ2
    if theta <= 0.3:
        categorical = 1
    else :
        categorical = 2

    #それぞれの値を決定
    if categorical == 1:
        mu = 0
        sigma = 2
    elif categorical == 2:
        mu = 2
        sigma = 6

    return mu , sigma

#パサー作成
parser = argparse.ArgumentParser()

parser.add_argument("--data",type=float)

#引数を作る
args = parser.parse_args()

theta = np.random.rand()


mu1 ,sigma1 = set_param(theta)

print(theta,mu1,sigma1)
