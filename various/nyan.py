# -*- coding:UTF-8 -*-

from re import A
from twython import Twython
import time
import datetime

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

api = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

print('ログインに成功しました')
print('2022/2/22 22:22:22にツイートします')
print('更新頻度は0.1秒です\n')

status = "にゃんにゃんにゃん(ฅ *`꒳´ * )ฅ\n#スーパー猫の日\n#猫の日\n\nCurrent_time: 2022/02/22 22:22:22"

print('set status----------------------------------')
print(status)
print('--------------------------------------------\n')

while True:
    
    time.sleep(0.1)

    dt_now = datetime.datetime.now()

    year = dt_now.year
    month = dt_now.month
    day = dt_now.day
    hour = dt_now.hour
    minute = dt_now.minute
    second = dt_now.second
    micro_second = dt_now.microsecond

    print("\rCurrent time :",year,"/",month,"/",day," ",hour,":",minute,":",second,".",micro_second, end="")

    if year == 2022 and month == 2 and day == 22 and hour == 22 and minute == 22 and second == 22:
        
        api.update_status(status=status)

        break