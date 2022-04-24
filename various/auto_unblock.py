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
follow = api.get_friends_ids(screen_name = sc_name, stringify_ids = True)

ptt_list = []
follow_list = follow['ids']

while True:
    for one in result['ids']:
        usr_id = one
        print(one)

        #安全装置
        if usr_id in ff_list:
            pass

        #自分がフォローしているアカウントは処理に回さない
        elif usr_id in follow_list:
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

    print("処理終了_処理したアカウントは以下の通りです")
    for one in ptt_list:
        print(one)
    print("処理アカウント数:", len(ptt_list))
    print("処理を通過したアカウントは以下の通りです")
    for one in result['ids']:
        print(one)
    print("通過総アカウント数:", len(result['ids']))
    break