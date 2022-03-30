from ast import Param
from enum import auto
import json, requests
from unittest import result
from requests_oauthlib import OAuth1

with open('token.json') as f:
    tokens = json.load(f)

    bearer_token = tokens['bearer_token']
    api_key = tokens['api_key']
    api_key_secret = tokens['api_key_secret']
    access_token = tokens['access_token']
    access_token_secret = tokens['access_token_secret']

auth = OAuth1(
    api_key,api_key_secret,access_token,access_token_secret
)

url = 'https://api.twitter.com/1.1/users/show/json'

params = {
    'screen_name' : 'jokowi'
}

result = requests.get(url, auth=auth, params=params)

print(result)