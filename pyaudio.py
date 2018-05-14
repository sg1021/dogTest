# -*- coding: utf-8 -*-
# マイク0番からの入力を受ける。一定時間(RECROD_SECONDS)だけ録音し、ファイル名：mono.wavで保存する。

import pyaudio
import _portaudio
import sys
import time
import wave

if __name__ == '__main__':
    chunk = 1024#特定の（記憶させる場所一つ一つに与えられる）フレームの数
    FORMAT = pyaudio.paInt16#16bitsフォーマットを変換
    CHANNELS = 1
    # サンプリングレート、マイク性能に依存
    RATE = 44100
    # 録音時間
RECORD_SECONDS = input('Please input recoding time>>>')

# pyaudio
p = pyaudio.Pyaudio()# sets up the portaudio system.

 # マイク0番を設定
input_device_index = 0
# マイクからデータ取得
#Open stream
#Streamとは、、for play or record audio.のためのツール
#新しいstreamを作るにはこのpyaudio.open()が必要
#ほしい引数をここで入れる
stream = p.open(format=FORMAT,#基本情報
                channels=CHANNELS,#チャンネル数
                rate=RATE,
                input=True,
                frames_per_buffer=chunk)#どれかから読み込んだデータを格納する為のバイト配列
                # おそらくframeとはデータ（音）を入れられる箱のことで1024はその数
all = []#おそらく初期化を行っている。これからこのリストにデータを入れてく
#Play stream
for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
   #Read stream（chunkはstreamのなかのものだからね）
    data = stream.read(chunk)#フレームの数を読み込む？データのバイト配列を読み込む？

    all.append(data)#allというリストオブジェクトの最後にdataを追加
    print("fin."+ data)
#Stop stream
stream.close()
data = ''.join(all) # 文字列リストのallを文字列に変換する
print(data)
out = wave.open('mono.wav', 'w') # ここからout.～はwave機能を表す。
# チャネル数を設定する
out.setnchannels(1)  # mono
# サンプルサイズを2バイトに設定する
out.setsampwidth(2)
# サンプリング　レートをRATEに設定
out.setframerate(RATE)
# dataに書き込まれた全フレーム数とframesに設定された値が一致しなかったらエラーを送る。
out.writeframes(data)
out.close()

# Close Pyaudio
p.terminate()
