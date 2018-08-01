#重みとバイアスで考える
import numpy as np
#入力を引数とする
def AND(x1,x2):
    #numpyを使うためにx,wの配列を作る
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    #numpyを使うためにx,wの配列を作る
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

