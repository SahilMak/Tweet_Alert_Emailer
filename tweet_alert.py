import tweepy
import time
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

c_key = 'consumer key'
c_secret = 'consumer secret'
a_token = 'access token'
a_secret = 'access token secret'

# Prompt user for keyword

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, data):
        try:
            # Extract tweet
            tweet = data.text
            # Extract tweet ID
            tweetID = data.id_str
            # Extract name
            name = data.author.name
            # Extract user name
            username = data.author.screen_name
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
