from pythonosc.udp_client import SimpleUDPClient
import time
import sys
import datetime

ip = "192.168.150.139"
port = 9000

client = SimpleUDPClient(ip, port)


client.send_message("/avatar/parameters/HR_onoff", 2)
client.send_message("/avatar/parameters/HR_string", 2)

try:

    while True:

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

        client.send_message("/avatar/parameters/HR_thp", int(htp))
        client.send_message("/avatar/parameters/HR_hp", int(hop))
        client.send_message("/avatar/parameters/HR_tp", int(mtp))
        client.send_message("/avatar/parameters/HR_op", int(mop))

        time.sleep(1)

except KeyboardInterrupt:

    client.send_message("/avatar/parameters/HR_thp", 0)
    client.send_message("/avatar/parameters/HR_hp", 0)
    client.send_message("/avatar/parameters/HR_tp", 0)
    client.send_message("/avatar/parameters/HR_op", 0)

    client.send_message("/avatar/parameters/HR_onoff", 0)
    client.send_message("/avatar/parameters/HR_string", 0)

    print("\n\n初期化しました\n終了します")

    sys.exit()



