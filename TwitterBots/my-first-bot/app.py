# from selenium import webdriver
# from selenium.webdriver.common.keys import keys
import tweepy
import time
from bot import *

consumer_key = "5cuobFCpWVs8Ax54b63oKLYG1"
consumer_secret = "gqcmRhTDwIPmPmLaUDUi0czqaK404kJ4iWruk9rhzFJTf5yVDO"
access_token = "1471870630790189062-Ou1pVtRWl2R8K3FMTnB54eApBpiHTf"
access_token_secret = "U06xnofd8RnNxvoJaQicytwaniV3LicmXYTbIhLQdgBqo"

keys = consumer_key, consumer_secret, access_token, access_token_secret

user = Bot(keys)

# prints ruchika's latest tweet
# user.get_last_tweet_by_username('fauxflwrchild')

print(user.my_id())
#
# chika = user.client.get_user(screen_name='fauxflwrchild')
#
# # chika = api.get_user(screen_name='fauxflwrchild')
# print(chika)
#
# tweet = chika.user_timeline(id = self.client_id, count = 1)[0]
# print(tweet.text)
# chika.get_last_tweet()

# # authorization of consumer key and consumer secret
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#
# # set access to user's access key and access secret
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth, wait_on_rate_limit=True) #, wait_on_rate_limit_notify=True)
# api = tweepy.API(auth)
# user = api.get_user(screen_name='fauxflwrchild')
# user = api.me()
# user = api.get_user(screen_name='1mawu1')

# print(user)



# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

# class TwitterBot:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.bot = webdriver.Firefox()
#
#     def login(self):
#         bot = self.bot
#         bot.get('https://twitter.com/i/flow/signup')
#         time.sleep(3)
#         email = bot.find_element_by_class_name('email-input')
#
# test = TwitterBot('1mawu', '1mawu1216!')
# ed.login()
