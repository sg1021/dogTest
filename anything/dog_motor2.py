#!/usr/bin/python
# -*- coding: utf-8 -*-

#ラズパイを操作するためのライブラリ
import RPi.GPIO as GPIO
#タイマーのライブラリ

import time

#ナンバリング設定（ＧＰＩＯ番号で）,GPIOの各ピンを指定するための方法

GPIO.setmode(GPIO.BCM)#これでGPIOピンが指定できるようになった。

#GPIOの4ピンを指定し、

#出力モードに変換し、

#ピン4に周波数50Hzを送り、pwmオブジェクトとする
go_out = 4
GPIO.setmode(go_out,GPIO.OUT)
servo = GPIO.PWM(go_out,50)

#初期設定（引数はDuty Cycle。Duty Cycleは0.0 - 100.0 のパーセンテージで指定する）


#(実際は0.5ms-2.4msの間で制御する。パルス全体は50Hzなので20msの幅があるから、
#2.5% - 12.0%のDuty Cycleで制御する。対応する角度は-90度-90度なので、
#Duty Cycleで2.5を指定したら-90度に軸が移動する)
servo.start(0.0)

#Duty Cycleを2.5%にすることで=-90°
#を0.5秒
servo.ChangeDutyCycle(2.5)
time.sleep(0.5)

#Duty Cycleを12.0%にすることで=-90°(1回転)

#を0.5秒
servo.ChangeDutyCycle(12.0)
time.sleep(0.5)


#Duty Cycleを2.5%にすることで=-90°（逆1回転）

#を0.5秒
servo.ChangeDutyCycle(2.5)
time.sleep(0.5)

#GPIOの操作を終える
GPIO.cleanup()
