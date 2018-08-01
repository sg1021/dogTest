#関数defと返値の勉強
import math

def menseki(r):
    #面積は
    s = math.pi * r**2
    return s



#半径を入力させるための変数
hankei = float(input("円の半径 = "))

#関数に入力した値を渡す
a = menseki(hankei)

print(a)


