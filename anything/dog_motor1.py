#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

#GPIOピンでいく
GPIO.setmode(GPIO.BCM)
#どちらのモードに設定されているか確認（勉強のために）
mode = GPIO.getmode() #"BCM" or "BOARD"　と表示される

#チャンネルのモード設定
#今回は複数のチャネルをリストでまとめてやる（勉強のために）
chan_list = [10,11]
GPIO.setup(chan_list,GPIO.OUT) #GPIO.IN は入力

#デジタル出力する　（アナログ（PWM）出力はPIN番号が少ないからやらない）
#さっき定義した出力ピンをHIGHにする
GPIO.output(chan_list,GPIO.HIGH)
#定義した10pinをHIGH,11pinをLOWにするプログラム（勉強のため）（使うかな？ ）
#GPIO.output(chan_list,(GPIO.HIGH, GPIO.LOW))

#アナログ出力（ＰＷＭ）をやってみる（勉強のため）
#チャネルと周波数とデューティ比を入力すればできる（らしい）
#たとえば、GPIO18に周波数1KHz,デューティ比50%でPWM出力する
#pwm = GPIO.PWM(18,1000) #設定
#(追加)設定した周波数で、データを取って0～180にmapすることもできる（方程式を作成）
#これを使って、
#pwm.start(50) #出力
#周波数変更したかったら、、
#pwm.ChangeFrequency(2000)
#デューティ比を変更したかったら、、
#pwm.ChangeDutyCycle(20)
#PWM出力を停止
#pwm.stop()

#GPIO入力（ポーリング:常に状況を確認すること ）
#プルダウン抵抗を用いて入力をやる（これも勉強のため）
#初期化
#GPIO.setup(22,GPIO.IN,pull_up_down = GPIO.PUD_UP)
#スイッチおして、1を検出した場合と、0を検出した場合
#if GPIO.input(22,pull_up_down):
    # 1を検出した場合
#else:
    # 0を検出した場合

#エッジ検出（使うとおもう、センサーとか）
#①エッジ検出待ち
#単なるポーリングエッジ検出よりもCPU資源を消費しないのが利点
#18番ピンの立ち上がり検出を待つ場合、、
#GPIO.wait_for_edge(18,GPIO.RISING)
#②エッジ検出イベントの取得（履歴取得orそのとき ）（センサ類に使える）
#ループのなかでボタンが押されていたかなどが確認できる
#使用する前のチャンネルのイベント登録 + ③コールバック関数(引数にcallback)
#④チャタリングをソフトウェアによって防ぐ
# RISING/FALLING/BOTH
#GPIO.add_event_detect(22,GPIO.RISING,callback=関数名,bouncetime=[ms])
#イベント発生状態の取得
#if GPIO.add_event_detected(22):
#    print("detected the edge")
#else:
#    print("no edge")
#イベント検出の解除
#GPIO.remote_event_detect(22)
#スクリプト終了時にこれをする
#GPIO.cleanup()
