from twython import Twython
import twython.exceptions

#token入力
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

#tokenのアカウントのスクリーンネーム
sc_name =""

#ブロ解処理に回したくないアカウントのIDを入力
ff_list = [
]

result = api.get_followers_ids(screen_name = sc_name, stringify_ids = True)

count = 0
ptt_list = []

while True:
    for one in result['ids']:
        usr_id = one
        print(one)

        if usr_id in ff_list:
            pass

        else:
            try:
                usr_data = api.show_user(id=usr_id)

                if usr_data['protected'] == True:
                    api.create_block(user_id = usr_id)
                    api.destroy_block(user_id = usr_id)

                    ptt_list.append(usr_data['id_str'])

            except twython.exceptions.TwythonError as e:
                print(e)

    count += len(result)

    print("処理終了_処理したアカウントは以下の通りです")
    for two in ptt_list:
        print(two)
    print("処理アカウント数:", count)
    print("処理を通過したアカウントは以下の通りです")
    for three in result['ids']:
        print(three)
    print("通過総アカウント数:", len(result['ids']))
    break