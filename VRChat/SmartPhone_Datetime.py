# -*- "coding : UTF-8" -*-

from pythonosc.udp_client import SimpleUDPClient
import time
import datetime
import sys

ip = "127.0.0.1"
port = 9000

client = SimpleUDPClient(ip, port)

time_onedigits = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9
}

time_twodigits = {
    0:10,
    1:11,
    2:12,
    3:13,
    4:14,
    5:15,
    6:16,
    7:17,
    8:18,
    9:19
}

time_threedigits = {
    0:20,
    1:21,
    2:22,
    3:23,
    4:24,
    5:25,
    6:26,
    7:27,
    8:28,
    9:29
}

time_fourdigits = {
    0:30,
    1:31,
    2:32,
    3:33,
    4:34,
    5:35,
    6:36,
    7:37,
    8:38,
    9:39
}

date_month = {
    1:40,
    2:41,
    3:42,
    4:43,
    5:44,
    6:45,
    7:46,
    8:47,
    9:48,
    10:49,
    11:50,
    12:51
}

day_onedigits = {
    0:52,
    1:53,
    2:54,
    3:55
}

day_twodigits = {
    0:56,
    1:57,
    2:58,
    3:59,
    4:60,
    5:61,
    6:62,
    7:63,
    8:64,
    9:65
}

day_of_week = {
    0:66, #月曜日　
    1:67,
    2:68,
    3:69,
    4:70,
    5:71,
    6:72 #日曜日
}

now_minutes = ""

try:
    while True:
        dt_now = datetime.datetime.now()

        month = dt_now.month
        day = str(dt_now.day)
        hours = dt_now.strftime("%H")
        minutes = dt_now.strftime("%M")
        weekday = dt_now.weekday()

        num_h = hours.zfill(2)
        num_m = minutes.zfill(2)

        num_day = day.zfill(2)

        time_onedigits_param = time_onedigits[int(num_h[-2])] #時刻一桁目
        time_twodigits_param = time_twodigits[int(num_h[-1])] #時刻二桁目
        time_threedigits_param = time_threedigits[int(num_m[-2])] #時刻三桁目
        time_fourdigits_param = time_fourdigits[int(num_m[-1])] #時刻四桁目

        date_month_param = date_month[month] #日付月

        day_onedigits_param = day_onedigits[int(num_day[-2])] #日付日一桁目
        day_twodigits_param = day_twodigits[int(num_day[-1])] #日付日二桁目

        day_of_week_param = day_of_week[weekday] #曜日

        param_list = [
            time_onedigits_param,
            time_twodigits_param,
            time_threedigits_param,
            time_fourdigits_param,
            date_month_param,
            day_onedigits_param,
            day_twodigits_param,
            day_of_week_param
        ]

        if now_minutes != minutes:
            now_minutes = minutes

            print("時刻更新")

            for i in param_list:
                #client.send_message("/avatar/parameters/SmartPhome_DatetimeParam", i)
                print(i)
                time.sleep(1)

        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()

