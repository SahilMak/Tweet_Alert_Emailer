import tweepy
import time
import smtplib
import tkinter
import tkinter.simpledialog
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

c_key = 'consumer key'
c_secret = 'consumer secret'
a_token = 'access token'
a_secret = 'access token secret'

e_address = 'email address'
e_password = 'email password'

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, data):
        try:
            # Extract tweet
            tweet = data.text
            # Extract tweet ID
            tweetID = data.id_str
            # Extract name
            name = data.author.name
            # Extract screen name
            screen_name = data.author.screen_name
            # Send gmail
            s = send_gmail(tweet, tweetID, name, screen_name)
            return True
        except BaseException as e:
            print(e)
            time.sleep(5)
    
    def on_error(self, status):
        print(status)

class send_gmail():
    
    def __init__(self, text, ID, user, username):
        # Create message header
        msg = MIMEMultipart()
        msg['From'] = e_address
        msg['To'] = e_address
        msg['Subject'] = "Tweet Alert"
        # Draft message body
        html = """\
        <html>
            <head></head>
            <body>
                <p>%s (@%s) has tweeted:<br>
                    %s
                </p>
            </body>
        </html>
        """ % (user, username, text)
        # Attach body to email
        msg.attach(MIMEText(html, 'html'))
        # Define server
        server = smtplib.SMTP('smtp.gmail.com', 587) #or 465
        server.starttls()
        # Login to email account
        server.login(e_address, e_password)
        # Send email
        text = msg.as_string()
        server.sendmail(e_address, e_address, text)
        server.quit

# Prompt user for keyword
root = tkinter.Tk()
root.withdraw()
keyword = []
keyword.append(tkinter.simpledialog.askstring('Keyword', 'Enter keyword'))
# Create authentication handler
auth = tweepy.OAuthHandler(c_key, c_secret)
# Set access token
auth.set_access_token(a_token, a_secret)
# Create the Twitter stream
stream = tweepy.Stream(auth, MyStreamListener())
# Search for keyword
stream.filter(track=[keyword])
