#! /usr/bin/env python3

# This simple script connects to the Twitter Streaming API using tweepy and
# tweets everytime when someone mentions the user in the tweet

import os
import time
import tweepy

class UserStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, status):
        try:
            self.api.update_status('Hey @{}! What\'s up?'.format(status.user.screen_name))
            print('Tweeted To: @{}'.format(status.user.screen_name))
        except Exception as e:
            print('Error Occured: {}'.format(e))

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return False # exit

    def on_timeout(self):
        print('Timeout...')
        return False # exit

def main():
    # Authentication
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    # Create the Stream
    userTweetStream = tweepy.Stream(auth=api.auth, listener=UserStreamListener(api))

    # Start the Stream
    userTweetStream.filter(track=['@' + api.me().screen_name])


if __name__ == '__main__': main()
