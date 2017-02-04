import os
import time
import tweepy

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

imageList = ['test.gif', 'test2.jpg', 'test3.jpg']

for image in imageList:
    api.update_with_media(image, '#MakingPeaceWithHumans')
    time.sleep(15)
