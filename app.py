#! /usr/bin/env python3

# This simple script connects to the Twitter Streaming API using tweepy and
# tweets everytime when someone mentions the user in the tweet

import os
import time
import tweepy

class UserStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

def main():
    # Authentication
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    # Create the Stream
    userTweetStream = tweepy.Stream(auth=api.auth, listener=UserStreamListener())

    # Start the Stream
    userTweetStream.userstream()



if __name__ == '__main__': main()
