#!/usr/bin/python
# -*- coding: utf-8 -*-

#ここでは、Serial通信の際に犬が毎回初期位置に戻らないようにするために、
#始めに、ポートをopenして、closeせずにSerial通信でwriteしていくプログラムを、
#試してみる。

import serial
import time
import socket
import xml.etree.ElementTree as ET ##XML形式をプログラムで扱うため

#ser = serial.Serial('/dev/ttyACM0',9600)
#time.sleep(2)

HOST = 'localhost'
PORT = 10500

#juliusの出力をdataという変数にXML型形式で受け取るためのプログラム
#ソケット接続によりクライアントを作り、Juliusサーバーと接続させる

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#juliusサーバ（TCP）に接続
client.connect((HOST,PORT))
#接続できたか確認する
print("connectted to Julius server")

try:
    #持ってきたデータを入れる変数dataを初期化
    data = ""
    # ポートを開けてあげる
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while 1:
        #データが受信されている場合。。。
        if "</RECOGOUT>\n." in data: #</RECOGOUT>は、Juliusからの認識結果のXML形式の文に入っているモノ
            # RECOGOUT要素以下をXML形式としてパース（解析してプログラムで扱えるようにする）
            # XMLを表す文字列からElement(要素)を作成するにはfromstring() 使う

            # ET.fromstring（ファイル）で受け取ったやつを解析する
            # rootnodeである<?xml version="1.0"?>を文字列で指定することでそれ以下のnodeをパースする。
            # （しかし、今回のXML文には<?xml version="1.0"?>はないので必要ないようにも感じる）
            # <RECOGOUT>要素の最後の「.」ないバージョンをパースしているとおもう

            root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):].replace("\n.", ""))
            # XML文を表示する
            #print(data)
            # 言葉を判別
            # WHYPO要素に絞る→"for whypo in whypo"

            for whypo in root.findall("./SHYPO/WHYPO"):
                # WHYPO要素の中の子ノードであるWORDに限定してパース（解析）
                command = whypo.get("WORD")

                # パースしたモノ（言葉）を表示する
                print(command)
                #もしおすわりだったら
                if command == u'おすわり':

                    # aduinoの立ち上がりまで2秒は必要
                    time.sleep(2)
                    # python2をつかっているのでbを省略できる
                    awrite = ser.write('a')  # 1byte
                    print(awrite)  # ここで１がprintされるとおもう
                    #ser.close()
                    # 新しいデータを優先させるためdataを初期化する
                    data = ""
                    break

            elif command == u'おて':

                #aduinoの立ち上がりまで2秒は必要
                time.sleep(2)

                # python2をつかっているのでbを省略できる
                bwrite = ser.write('b')  # 1byte
                print(bwrite)  # ここで１がprintされるとおもう
                #ser.close()
                #古いデータをdataに残さないように（ループしてしまう）
                data = ""
                break
            else:
                print("Unknown")
                data = data + client.recv(1024)

except KeyboardInterrupt: #CTRL+Cで終了
    ser.close()
    print("KeyboardInterrupt occured.")
    client.close()