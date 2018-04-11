import tweepy as tp


def get_auth():
    key_filename = "D:\SchFiles\大三下\社交媒体大数据\TwitterAppKey\keys.txt"

    with open(key_filename) as f:
        line = f.readline()
        strlist = line.split(',')
        consumer_key = strlist[0]
        consumer_secret = strlist[1]
        access_token = strlist[2]
        access_secret = strlist[3]

        # print('consumer_key:', consumer_key)
        # print('consumer_secret: ', consumer_secret)
        # print('access_token: ', access_token)
        # print('access_secret: ', access_secret)

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return auth
