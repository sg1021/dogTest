import socket
import wiringpi
import time
import sys

servo1_pin = 12
servo2_pin = 13

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(servo1_pin,2) #pwm制御するから3つ目のpwm(2)
wiringpi.pinMode(servo2_pin,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetRange(1024)
wiringpi.pwmSetClock(375)

 #角度と言葉でpin1,2を動かす
def ServoMyservo(set_degree,word):
    if word == "ote":
        if(set_degree <= 90 and set_degree >= -90):
            move_deg = int(81 + 41/90 * set_degree )
            wiringpi.pwmWrite(servo1_pin,move_deg)

    elif word == "osuwari":
        if(set_degree <= 90 and set_degree >= -90):
            move_deg = int(81 + 41 / 90 * set_degree)
            wiringpi.pwmWrite(servo2_pin, move_deg)


def word(recv_data):

def main():
    host = 'localhost'
    port = 10500

    #socketの引数ではどうやって通信するかをきめるもの
    # socket(int domain, int type, int protocol)
    #domainによってFamily typeを選択する。その中のどのtypeか
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # http://www.fireproject.jp/feature/c-language/socket/basic.html
    client.connect((host,port))

    try:
        data = ""
        while 1:
            if ''




