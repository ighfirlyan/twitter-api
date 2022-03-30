#import semua library yang kalian butuhkan disini

import json, tweepy

#sel ini digunakan untuk membaca tokens kalian. simpan berkas token.json pada folder yang sama dengan file tugas ini

with open("token.json") as f:
  tokens = json.load(f)

bearer_token = tokens['bearer_token']
api_key = tokens['api_key']
api_key_secret = tokens['api_key_secret']
access_token = tokens['access_token']
access_token_secret = tokens['access_token_secret']

tokens.keys()

#buat variabel authentikasi dan api

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Buatlah sebuah fungsi dengan nama user_timeline_scraper()
#fungsi tersebut memiliki input username dari user
#Fungsi ini berguna untuk mengambil 10 tweet yang berada di timeline user.
#gunakan metode Cursor untuk tugas ini
#gunakan tweet_mode --> extended

def user_timeline_scraper(username):
    response = tweepy.Cursor(api.user_timeline, screen_name = username, tweet_mode = 'extended').items(10)
    for i in response:
        print(i.full_text)
        print("----------------------------------------")

username = "jokowi"
user_timeline_scraper(username)