#_*_ coding: utf-8 _*_
#マイク0番からの入力を受ける。一定時間（RECROD_SECONDS）だけ録音し、ファイル名：mono.wavで保存する

import pyaudio
import sys
import time
import wave
import requests
import os
import json
import subprocess


def recognize():#音声認識
    #音声を分析してくれるAPI先のurl
    url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY={}".format("51794a5853586e527a476c384651626942466c4f3668786a6c6f4c4d5370776e7732355649702f5a6e4f43")
    #録音した音声（PATH）をバイナリモードに変換して展開してから"a"に保管し、
    #"v"によって発音区間検出処理を行い、"on"で無音のとこを感知しないようにする
    files = {"a":open(PATH,"rb"),"v":"on"}
    #音声認識してくれるurl先に引数であるfilesを送信
    r = requests.post(url,files=files)
    #返ってきた"text"("音声認識結果の文字列")がJSON形式なのでjsonでキャッチ
    #（docomoのAPIがjsonを推奨しているためと考えられる）
    message = r.json('text')
    #認識した文字列をコンソールに表示
    print(message)
    #ほかの関数でこの戻り値を使いたいのでreturnで返す
    return message

def dialogue(message = "こんにちは"):
    url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY={}".format(APIKEY)
    #キャラ設定
    payload = {
        "utt": message,
        "context": "",
        "nickname": "光",
        "nickname_y": "ヒカリ",
        "sex": "女",
        "bloodtype": "B",
        "birthdateY": "1997",
        "birthdateM": "5",
        "birthdateD": "30",
        "age": "16",
        "constellations": "双子座",
        "place": "東京",
        "mode": "dialog",
        "t": 20
    }
    # (リクエストパラメータとして文字列を送ることに対するMIMEタイプは指定されていない。おそらくJSON)
    #だから辞書型のpayloadデータをjson形式の文字列に変換して、url先に送信
    r = requests.post(url,data=json.dumps(payload))
    print(r.json()['utt'])
    return r.json()['utt']

#def talk(message="こんにちは",card=1,device=0):
#   res = subprocess.check_output( '/home/pi/aquestalkpi/AquesTalkPi " ' + message.encode('utf-8') + ' " | aplay -Dhw:{},{}', stderr=subprocess.STDOUT, shell=True)


if __name__ == '__main__':
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    PATH = '/home/pi/mono.wave'
    APIKEY = "51794a5853586e527a476c384651626942466c4f3668786a6c6f4c4d5370776e7732355649702f5a6e4f43"
    CARD = 2#OUTPUTの指定
    DEVICE = 0
    #サンプリンググレート（1秒あたりのサンプリング数）、マイク性能に依存
    RATE = 48000
    #録音時間
    RECORD_SECONDS = int(input('Please input recording time>>>'))

    #pyaudio
    p = pyaudio.PyAudio()

    #マイク0番を設定
    input_device_index = 0
    #マイクからデータ取得
    # Open stream
    # Streamとは、、for play or record audio.のためのツール
    # 新しいstreamを作るにはこのpyaudio.open()が必要
    # ほしい引数をここで入れる
    stream = p.open(format = FORMAT,#基本情報
                    channels = CHANNELS,#チャンネル数
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)#どれかから読み込んだデータを格納する為のバイト配列
                    # おそらくframeとはデータ（音）を入れられる箱のことで1024はその数

    all = []#初期化を行っている。これからこのリストにデータを入れてく
    #play stream
    for i in range(0,int(RATE / chunk * RECORD_SECONDS)):
        # Read stream（chunkはstreamのなかのものだからね）
        data = stream.read(chunk)#フレームの数を読み込む
        all.append(data)#allというリストオブジェクトの要素の最後にdataを追加

    #stop stream
    stream.close()
    #data = ''.join(all)#文字列リストのallを文字列に変換する。108行目のdataは数値じゃないといけないので。
    out = wave.open(PATH,'w')#ここからout.～はwave機能を表す。
    #チャンネル数の設定
    out.setnchannels(1)#mono
    #サンプルサイズを2バイトに設定する
    out.setsampwidth(2)#16bits
    #サンプリングレートをRATEに設定
    out.setframerate(RATE)
    # dataに書き込まれた全フレーム数とframesに設定された値が一致しなかったらエラーを送る。
    out.writeframes(data)
    out.close()
    #Close Pyaudio
    p.terminate()

    #
    message = recognize()
    talk_message = dialogue(message)
    #talk(talk_message,CARD,DEVICE)




