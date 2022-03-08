# -*- coding:UTF-8 -*-

import os
import signal
import sys
import subprocess
import time
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

try:
    while True:

        def print_handler(address, *args):
            global prec1
            global prec2

            #print(f"{address}: {args}")

            if address == "/avatar/parameters/HR_OSC" and str(args) == "(1,)":
                print("心拍数呼び出し")
                cmd1 = "exec python osc_heart.py"
                prec1 = subprocess.Popen(cmd1, shell=True)

                print("PID = {}".format(prec1.pid))

            if address == "/avatar/parameters/HR_OSC" and str(args) == "(2,)":
                print("心拍数終了")
                prec1.send_signal(signal.SIGINT)
                time.sleep(1)
                prec1.kill()
                print("正常にキルされました")

            if address == "/avatar/parameters/HR_OSC" and str(args) == "(3,)":
                print("現在時刻呼び出し")
                cmd2 = "exec python osc_time.py"
                prec2 = subprocess.Popen(cmd2, shell=True)

                print("PID = {}".format(prec2.pid))

            if address == "/avatar/parameters/HR_OSC" and str(args) == "(4,)":
                print("現在時刻終了")
                prec2.send_signal(signal.SIGINT)
                time.sleep(1)
                prec2.kill()
                print("正常にキルされました")

        def default_handler(address, *args):
            print(f"DEFAULT {address}: {args}")

        dispatcher = Dispatcher()
        dispatcher.map("/avatar/*", print_handler)
        dispatcher.set_default_handler(default_handler)

        ip = "192.168.150.106"
        port = 9001

        server = BlockingOSCUDPServer((ip, port), dispatcher)
        server.serve_forever()

except KeyboardInterrupt:
    sys.exit()
