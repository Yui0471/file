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
sc_name = input('>>> ')
print('対象アカウント: ' + sc_name)
print('-'*30)
time.sleep(1)
print('[処理開始]FF内アカウントリストの作成を開始します')
time.sleep(1)

follower_id_list = api.get_followers_ids(screen_name = sc_name, stringify_ids = True)
follow_id_list = api.get_friends_ids(screen_name=sc_name, stringify_ids = True)

ff_id_list = set(follow_id_list['ids']) & set(follower_id_list['ids'])

count = 0
rate = 0
ff_list = []
today = datetime.datetime.fromtimestamp(time.time())
file_name = today.strftime('%Y%m%d%H%M%S') + '.txt'
f = open(file_name, 'w', encoding='UTF-8')
f.write('friend_list = [' + '\n')

while True:
    for one in ff_id_list:
        try:
            if rate != 800: #レート制限
                user_data = api.show_user(user_id=one)

                write_data = '#' + user_data['name'] + ':' + user_data['screen_name'] + '\n"' + one + '",\n'
            
                ff_list.append(user_data['name'])
                count += 1
                rate += 1
                f.write(write_data)

                print('\r' + str(one), end='')

            else:
                print('\n[warning]レート制限に達しました。回復まで15分かかります\n少々お待ちください')
                for i in range(900, 0, -1):
                    print('\r残り' + str(i) + '秒', end='')
                    time.sleep(1)
                print('\n[制限回復]処理を再開します')
                rate = 0
                time.sleep(2)

        except twython.exceptions.TwythonError as e:
            print(e)
            break
    
    time.sleep(1)
    print('-'*30)
    print('\n[処理終了]FF内アカウントリストのファイル書き出し処理を終了しました')
    time.sleep(1)
    print('書き出しを実行したアカウントは以下の通りです')
    time.sleep(1)
    for one in ff_list:
        print(one)
        time.sleep(0.01)
    time.sleep(1)
    print('-'*30)
    print('計' + str(count) + 'アカウントを記録しました')
    time.sleep(1)
    f.close()
    print('出力ファイル名:' + file_name)
    print('同ディレクトリに正常に出力されました')
    print('[プログラム終了]')
    break