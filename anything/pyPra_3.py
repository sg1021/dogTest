#コンストラクターの使い方（わかんね）
from time import sleep
from turtle import *
t = Turtle()

class KameClass:
    name = "" #名前が入る変数を初期化

    # 始めにここに来る。あと、selfに h が、nに"おれっち"が入る
    #これはクラスを作ったときに、始めに実行してほしいプログラムがあるときに使う

    #犬では、「おすわり」→「よし」→もとに→「おて」or
    #「おすわり」（1周だけされるようにすればいい）→「おて」→「ゴー」
    def __init__(self,n):
        #変数を初期化
        self.name = n

    def add_kame(self,s):
        print(self.name + str(s) + "ステップ移動")
        t.fd(s)
        sleep(1)


h = KameClass("おれっち")
h.add_kame(50)

