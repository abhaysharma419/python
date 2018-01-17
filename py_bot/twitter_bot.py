import tweepy
import os
import time

consumer_key=''
consumer_secret=''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

os.chdir('models')

for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
