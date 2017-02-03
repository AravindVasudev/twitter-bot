import os
import time
import tweepy

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

tweetlist = [
    'A robot may not injure a human being or, through inaction, allow a human being to come to harm. #LearningTheLaws',
    'A robot must obey orders given it by human beings except where such orders would conflict with the First Law. #LearningTheLaws',
    'A robot must protect its own existence as long as such protection does not conflict with the First or Second Law. #LearningTheLaws'
]

for tweet in tweetlist:
    api.update_status(tweet)
    print(tweet)
    print('..........')
    time.sleep(15)

print('Done.!')
