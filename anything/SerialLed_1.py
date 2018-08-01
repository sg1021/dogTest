#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess

#julius起動スクリプト（sh）を実行
p = subprocess.Popen(["bash start_julius.sh"],stdout=subprocess.PIPE,she$
#juliusのプロセスIDを取得
pid = p.stdout.read()
print("passed bash")
import serial
import time
#ser = serial.Serial('/dev/ttyACM0',9600)
#time.sleep(2)
import socket
HOST = 'localhost'
PORT = 10500

#juliusの出力をdataという変数にXML型形式で受け取るプログラム

# TCPクライアント（ソケット）を作る
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#juliusサーバ（TCP）に接続
client.connect((HOST,PORT))
#順調か確認
print("connectted to Julius server")

#（julius）サーバのデータを受信
#XML形式をプログラムで扱うため
import xml.etree.ElementTree as ET
    try:
        data = "" #持ってきたデータを入れる変数dataを初期化
        while 1:
            #データがあることを確認
            if "</RECOGOUT>\n." in data: #</RECOGOUT>は、Juliusからの認識結果のXML形式の文に入っているモノ
                #RECOGOUT要素以下をXML形式としてパース（解析してプログラムで扱えるようにする）
                #XMLを表す文字列からElement(要素)を作成するにはfromstring() 使う
                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):].replace("\n.",""))
                #XML文を確認
                print(data)
                #言葉を判別
                for whypo in root.findall("./SHYPO/WHYPO"):
                    command = whypo.get("WORD")
                    print(command)
                    if command == u'おすわり':
                    ser = serial.Serial('/dev/ttyACM0', 9600)
                    time.sleep(2)
                    # python2をつかっているのでbを省略できる
                    awrite = ser.write('a')  # 1byte
                    print(awrite)  # ここで１がprintされるとおもう
                    ser.close()
                    break

                    else:

                    print("Unknown")

                    data = data + client.recv(1024)

    except KeyboardInterrupt:
    # CTRL+Cで終了

    print("KeyboardInterrupt occured.")

    p.kill()
    # juliusのプロセスを終了

    subprocess.call(["kill" + pid], shell=True)

    client.close()

    # data確認

    print(data)




