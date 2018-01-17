import tweepy
import os
import time

consumer_key='H5jys7BWwEHON4Ca4i5PnLGiq'
consumer_secret='ZDof7N71abIZB91U42OVRSBjiJsP9m6vrvUkd5Pkw4naq0NPSg'

access_token='953634970827874304-x60xHcoMOvOrS2SBIlV8pVlhugnXuGL'
access_token_secret='RmVKvFvz2aQ8P5cLUy18UacSbeg0KQTT7uc3kNx5m8lW0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

os.chdir('models')

for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)