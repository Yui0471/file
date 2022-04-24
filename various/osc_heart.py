# -*- coding:UTF-8 -*-

#Linux環境でのみ動作します
#動作確認端末:POLAR Verity Sense

from bluepy import btle
from pythonosc.udp_client import SimpleUDPClient
import time
import sys
import datetime

ip = "yourIP"
port = 9000
params = ""

client = SimpleUDPClient(ip, port)

client.send_message("/avatar/parameters/HR_onoff", 1)
client.send_message("/avatar/parameters/HR_string", 1)

try:
    while True:

        class MyDelegate(btle.DefaultDelegate):

            def __init__(self,params):
                print(params)

                btle.DefaultDelegate.__init__(self)

            def handleNotification(self, cHandle, data):
                #print(cHandle)
                #print(data)

                heartrate = int.from_bytes(data, byteorder='big')
                print("心拍数:", heartrate)

                #client.send_message("/avatar/parameters/heartrate", heartrate)

                HR = str(heartrate).zfill(3)

                hr_hp = HR[-3]
                hr_tp = HR[-2]
                hr_op = HR[-1]

                client.send_message("/avatar/parameters/HR_hp", int(hr_hp))
                client.send_message("/avatar/parameters/HR_tp", int(hr_tp))
                client.send_message("/avatar/parameters/HR_op", int(hr_op))
        


                if heartrate >= 30 and heartrate <= 100:
                    print("100↓")
                    client.send_message("/avatar/parameters/ear_L", float('0.00'))
                    client.send_message("/avatar/parameters/ear_R", float('0.00'))
                    client.send_message("/avatar/parameters/HR_tail", 1)

                if heartrate >= 100 and heartrate <= 120:
                    print("100~120")
                    client.send_message("/avatar/parameters/ear_L", float('0.00'))
                    client.send_message("/avatar/parameters/ear_R", float('0.50'))
                    client.send_message("/avatar/parameters/HR_tail", 1)

                if heartrate >= 121 and heartrate <= 130:
                    print("121~130")
                    client.send_message("/avatar/parameters/ear_L", float('0.20'))
                    client.send_message("/avatar/parameters/ear_R", float('0.80'))
                    client.send_message("/avatar/parameters/HR_tail", 0)


                if heartrate >= 131 and heartrate <= 140:
                    print("131~140")
                    client.send_message("/avatar/parameters/ear_L", float('0.80'))
                    client.send_message("/avatar/parameters/ear_R", float('1.00'))
                    client.send_message("/avatar/parameters/HR_tail", 0)

                if heartrate >= 141 and heartrate <= 200:
                    print("141↑")
                    client.send_message("/avatar/parameters/ear_L", float('1.00'))
                    client.send_message("/avatar/parameters/ear_R", float('1.00'))
                    client.send_message("/avatar/parameters/HR_tail", 0)

        p = btle.Peripheral("a0:9e:1a:ad:06:6b")
        p.withDelegate(MyDelegate(params))

        handle = 40
        p.writeCharacteristic(handle+1, b'\x01\x00', True)

        TIMEOUT = 1.0
        while True:
            if p.waitForNotifications(TIMEOUT):
                continue
            print('wait...')

except KeyboardInterrupt:
    print('初期化')

    client.send_message("/avatar/parameters/HR_hp", 0)
    client.send_message("/avatar/parameters/HR_tp", 0)
    client.send_message("/avatar/parameters/HR_op", 0)

    client.send_message("/avatar/parameters/ear_L", float('0.00'))
    client.send_message("/avatar/parameters/ear_R", float('0.00'))

    client.send_message("/avatar/parameters/HR_onoff", 0)
    client.send_message("/avatar/parameters/HR_string", 0)
    client.send_message("/avatar/parameters/HR_tail", 0)

    p.writeCharacteristic(handle+1, b'\x00\x00', True)
    p.disconnect()

    sys.exit()

