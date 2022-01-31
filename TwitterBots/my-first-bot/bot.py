import tweepy
import time

class Bot:
    def __init__(self, keys):
        self._consumer_key = keys[0]
        self._consumer_secret = keys[1]
        self._access_token = keys[2]
        self._access_secret = keys[3]

        try:
            auth = tweepy.OAuthHandler(self._consumer_key,
                                       self._consumer_secret)
            auth.set_access_token(self._access_token, self._access_secret)

            self.client = tweepy.API(auth, wait_on_rate_limit=True)
            if not self.client.verify_credentials():
                raise tweepy.TweepError
        except tweepy.TweepError as e:
            print('ERROR : connection failed. Check your OAuth keys.')
        else:
            print('Connected as @{}, you can start to tweet !'.format(self.client.verify_credentials().screen_name))
            self.client_id = self.client.verify_credentials().id
####MEEEE############################################################################
    def me(self):
        return self.client.verify_credentials()
    def my_id(self):
        return self.me().screen_name
    def get_my_last_tweet(self):
        tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
        print(tweet.text)

####FOLLOWERS###############################################################################
    def

####TWEETS###############################################################################


    def get_last_tweet_by_username(self, username):
        tweet = self.client.user_timeline(screen_name = username, count = 1)[0] # Get the last tweet
        # By default api.user_timeline() gets the last 20 tweets, but you can specify it
        # with the count parameter
        ### An object of class Status (tweepy.models.Status)
        print(tweet.created_at) # Print the datetime object for the tweet
        print(tweet.text) # Print the text of the tweet
        print(tweet.in_reply_to_screen_name) # Print the username of the user the
        # the tweet is replying to, it is None if the tweet is not a reply
        return tweet
