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

def NAND(x1,x2):
    #numpyを使うためにx,wの配列を作る
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y
a = XOR(0,0),XOR(0,1),XOR(1,0),XOR(1,1)
print(a)









