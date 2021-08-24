from twython import Twython
import twython.exceptions
import time, datetime

consumer_key = input('consumer_key >>> ')
consumer_secret = input('consumer_secret >>> ')
access_token = input('access_token >>> ')
access_token_secret = input('access_token_secret >>> ')

api = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

print('[プログラム開始]')
time.sleep(1)
print('探索対象アカウントのスクリーンネームを入力してください')
sc_name = input('>>> @')
print('対象アカウント: @' + sc_name)
print('-'*30)
time.sleep(1)
print('[処理開始]FF内アカウントリストの作成を開始します')
time.sleep(1)

user_data = api.show_user(screen_name=sc_name)
follow_count = user_data['friends_count']
followers_count = user_data['followers_count']

try:
    if follow_count >= followers_count:
        f_id = api.get_followers_ids(screen_name=sc_name,stringify_ids=True)

    else:
        f_id = api.get_friends_ids(screen_name=sc_name,stringify_ids=True)
    
    f_id_list = list(f_id['ids'])

    if follow_count >= followers_count:
        f_list = api.get_friends_list(screen_name=sc_name,count=200)

    else:
        f_list = api.get_followers_list(screen_name=sc_name,count=200)

    f_user_list = {}

    while True:
        for one in f_list['users']:
            id_str = one['id_str']
            user_name = one['screen_name'] + '/' + one['name']
            f_user_list[id_str] = user_name

        if f_list['next_cursor'] == 0:
            break

        cursor = f_list['next_cursor']
        f_list = api.get_friends_list(screen_name=sc_name,count=200,cursor=cursor)

except twython.exceptions.TwythonError as e:
    print(e)

ff_id_list = set(f_user_list) & set(f_id_list)

today = datetime.datetime.fromtimestamp(time.time())
file_name = today.strftime('%Y%m%d%H%M%S') + '.txt'
f = open(file_name, 'w', encoding='UTF-8')
f.write('friend_list = [' + '\n')

for one in ff_id_list:

    write_data = '#' + f_user_list[one] + '\n"' + one + '",\n'
    f.write(write_data)

    print('\r' + str(one), end='')

f.close()

print('\n' + '-'*30)
print('\n[処理終了]FF内アカウントリストのファイル書き出し処理を終了しました')
time.sleep(1)
print('書き出しを実行したアカウントは以下の通りです')
time.sleep(1)
for one in ff_id_list:
    print(f_user_list[one])
    time.sleep(0.05)
print('-'*30)
print('計' + str(len(ff_id_list)) + 'アカウントを記録しました')
time.sleep(1)
print('出力ファイル名:' + file_name)
print('同ディレクトリに正常に出力されました')
print('[プログラム終了]')