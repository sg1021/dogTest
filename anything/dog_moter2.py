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
