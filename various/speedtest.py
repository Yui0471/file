import subprocess
import json
import datetime
import time
import sys

def speedtest():
    try:
        process = subprocess.run(['speedtest', '--json'], capture_output=True)
        data = json.loads(process.stdout)
        return data
    except:
        return False

def bit_to_mbit(bit):
    return bit / 1024 / 1024

def data_print(data1, data2, data3):
    f = open("speedtest_data.txt", "a", encoding="UTF-8")
    datalist = []
    datalist.append(data1)
    datalist.append(" ")
    datalist.append(data3)
    datalist.append("\n")
    datalist.append(data2)
    datalist.append("\n")
    f.writelines(datalist)
    f.close()

while True:
    dt_now = datetime.datetime.now()
    time_month = dt_now.month
    time_day = dt_now.day
    time_hour = dt_now.hour
    time_minute = dt_now.minute

    if True:#(0 == time_minute) or (30 == time_minute):
        result = speedtest()
        time_now = str(time_month) + "/" + str(time_day) + " " + str(time_hour) + ":" + str(time_minute)

        if not result:
            data_print(time_now, "ERROR", "ERROR")

        result_print = str(bit_to_mbit(result["download"])) + " " + str(bit_to_mbit(result["upload"]))
        print(result_print)

        data_print(time_now, json.dumps(result), result_print)

        time.sleep(1800)





