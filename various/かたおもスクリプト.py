from twython import Twython
import time
import sys

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

print('どちらを使用しますか？')
appcheck = input('片思いチェッカー/片思われチェッカー (1/2) >>> ')

print('探索対象アカウントのスクリーンネームを入力してください')
sc_name = input('>>> @ ')
print('対象アカウント: @ ' + sc_name)
print('-'*30)
time.sleep(1)
if appcheck == '1':
    print('[処理開始]片思いアカウントリストの作成を開始します')
    kataomoi = True
    kataomoware = False

elif appcheck == '2':
    print('[処理開始]片思われアカウントリストの作成を開始します')
    kataomoi = False
    kataomoware = True

else:
    print('[error!]入力が間違っています。やり直してください')
    sys.exit()

time.sleep(1)
print('[データ取得中……]')

follow = api.get_friends_ids(id=sc_name)
followers = api.get_followers_ids(id=sc_name)

follow_id = follow['ids']
followers_id = followers['ids']

if kataomoi:
    account_ids = (set(follow_id) - set(followers_id))

if kataomoware:
    account_ids = (set(followers_id) - set(follow_id))

user_name = []
write_data = []

for one in account_ids:
    user_data = api.show_user(id=one)
    write_data.append(user_data['name'] + '\n' + str(one) + ' : ' + user_data['screen_name'] + '\n')
    user_name.append(user_data['name'])

if kataomoi:
    file_name = 'kataomoi.txt'

if kataomoware:
    file_name = 'kataomoware.txt'

f = open(file_name, 'w', encoding='UTF-8')

print('[データ取得完了]取得データを出力します')

for one in write_data:
    f.write(one)

f.close()

print('-'*30)
print('[処理終了]アカウントリストのファイル書き出し処理を終了しました')
time.sleep(1)
print('書き出しを実行したアカウントは以下の通りです')
time.sleep(1)
for one in user_name:
    print(one)
    time.sleep(0.01)
print('-'*30)
print('計' + str(len(account_ids)) + 'アカウントを記録しました')
time.sleep(1)
print('出力ファイル名:' + file_name)
print('同ディレクトリに正常に出力されました')
print('[プログラム終了]')