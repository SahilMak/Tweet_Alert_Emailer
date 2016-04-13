import tweepy
import time
import smtplib
from email.mime.text import MIMEText

c_key = 'consumer key'
c_secret = 'consumer secret'
a_token = 'access token'
a_secret = 'access token secret'

# Prompt user for keyword

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, data):
        try:
            # Extract tweet
            tweet = data.text.split(", 'text': '")[0].split("', 'is_quote_status'")[0]
            #Extract tweet ID
            tweetID = data.text.split(", id=")[0].split(", ")[0]
            print(tweet)
            return True
        except BaseException as e:
            print(e)
            time.sleep(5)
    
    def on_error(self, status):
        print(status)

# Create authentication handler
auth = tweepy.OAuthHandler(c_key, c_secret)
# Set access token
auth.set_access_token(a_token, a_secret)
# Create the Twitter stream
stream = tweepy.Stream(auth, MyStreamListener())
# Search for keyword
stream.filter(track=[keyword])
