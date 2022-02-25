from pythonosc.udp_client import SimpleUDPClient
import time
import sys
import datetime

msg = """
//////////////////////////////////////////
VRChat Open Sound Control 
                  時刻表示プログラム

2022/02/20 : 風庭ゆい

注 : 対応したアバターのみ効力を発揮します

//////////////////////////////////////////
"""

ip = "127.0.0.1"
port = 9000

client = SimpleUDPClient(ip, port)

print(msg)

print('初期化します')

#初期化

client.send_message("/avatar/parameters/hour_tp", 10)
client.send_message("/avatar/parameters/hour_op", 10)
client.send_message("/avatar/parameters/minute_tp", 10)
client.send_message("/avatar/parameters/minute_op", 10)
client.send_message("/avatar/parameters/dot", 10)

time.sleep(0.3)

client.send_message("/avatar/parameters/hour_tp", 0)
client.send_message("/avatar/parameters/hour_op", 0)
client.send_message("/avatar/parameters/minute_tp", 0)
client.send_message("/avatar/parameters/minute_op", 0)
client.send_message("/avatar/parameters/dot", 0)

time.sleep(0.3)

print('時刻表示を開始します\n')
print('Ctrl+Cで終了します\n')

try:

    while True:

        client.send_message("/avatar/parameters/dot", 0)

        time.sleep(0.5)

        dt_now = datetime.datetime.now()

        hours = dt_now.strftime('%H')
        minutes = dt_now.strftime('%M')
        seconds = dt_now.strftime('%S')

        num_h = hours.zfill(2)
        num_m = minutes.zfill(2)
        num_s = seconds.zfill(2)

        htp = num_h[-2]
        hop = num_h[-1]

        mtp = num_m[-2]
        mop = num_m[-1]

        stp = num_s[-2]
        sop = num_s[-1]

        print("\r現在時刻:", htp,hop,":",mtp,mop,":",stp,sop, end="")

        client.send_message("/avatar/parameters/hour_tp", int(htp))
        client.send_message("/avatar/parameters/hour_op", int(hop))
        client.send_message("/avatar/parameters/minute_tp", int(mtp))
        client.send_message("/avatar/parameters/minute_op", int(mop))

        client.send_message("/avatar/parameters/dot", 1)

        time.sleep(0.5)

except KeyboardInterrupt:

    client.send_message("/avatar/parameters/hour_tp", 10)
    client.send_message("/avatar/parameters/hour_op", 10)
    client.send_message("/avatar/parameters/minute_tp", 10)
    client.send_message("/avatar/parameters/minute_op", 10)
    client.send_message("/avatar/parameters/dot", 0)
    print("\n\n初期化しました\n終了します")

    time.sleep(1)

    sys.exit()



