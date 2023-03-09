import tweepy
from logger import *
import requests


def parse(api_key, api_key_secret, access_token, access_token_secret, username):
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    user = client.get_user(username=username, user_auth=True)
    tweet_text = client.get_users_tweets(id=user.data.id, max_results=25, user_auth=True)
    print(str(tweet_text))
    return str(tweet_text)


def find_(link, text):
    lik = ''
    le = len(link)
    if text.find(link) != -1:
        k = text.find(link) + le
        while text[k] != '>' and text[k] != ' ' and text[k] != '\n':
            lik += text[k]
            k += 1
        return lik
    else:
        return '-1'


def disc_link(text):
    arr = []
    # print(text)
    code = ''
    k = 0
    # while code not in arr:
    code = find_('https://t.co/', text[k:])
    if code != '-1':
        arr.append(code)
        print('https://t.co/' + code)
        r = requests.get('https://t.co/' + code)
        link = r.url
        print(link)
        if 'discord' in link:
            if 'https://discord.com/invite/' in link:
                return link[27:]
            else:
                link = 'https://t.co/'
                lik = ''
                le = len(link)
                if text.find(link) != -1:
                    k = text.find(link) + le
                    while text[k] != '>' and text[k] != ' ' and text[k] != '\n':
                        k += 1
                    while text[k] == ' ':
                        k+=1
                    while text[k] != '>' and text[k] != ' ' and text[k] != '\n':
                        lik += text[k]
                        k += 1
                    return lik

        else:
            return '-1'


def get_inv_code(text):
    code = disc_link(text)

    logger.info(code)  # https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be
    return code

    # https: // t.co / UoeB6DK0hJ

    # lik2 = find_('discord.gg/', text)
    # lik3 = find_('discord.com/invite/', text)
