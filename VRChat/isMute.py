# -*- coding : UTF-8 -*-

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient
#import pyautogui
import sys
import time


ip = "127.0.0.1"
port = 9000

client = SimpleUDPClient(ip, port)

#input("クリック位置でenter")
#click_point = pyautogui.position()

try:
    while True:
        def print_handler(address, *args):
            #global click_point
            print(f"{address}: {args}")

            if address == "/avatar/parameters/isMute": #ボタンが押された!
                client.send_message("/input/Voice", 0) #一度0を書き込まないといけない模様。なんで？？
                time.sleep(0.1)
                client.send_message("/input/Voice", 1) #ミュートにする
                time.sleep(0.1)
                client.send_message("/input/Voice", 0)
                print("ミュート")
                
            

            #elif address == "/avatar/parameters/isExit": #終了
                #pyautogui.moveTo(click_point)
                #pyautogui.click()
                #print("実行")


                
        def default_handler(address, *args):
            print(f"DEFAULT {address}: {args}")

        dispatcher = Dispatcher()
        dispatcher.map("/avatar/*", print_handler)
        dispatcher.set_default_handler(default_handler)

        ip = "127.0.0.1"
        port = 9001

        server = BlockingOSCUDPServer((ip, port), dispatcher)
        server.serve_forever()

except KeyboardInterrupt:
    sys.exit()
