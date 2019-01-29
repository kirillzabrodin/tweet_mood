import json
import tweepy
from tweepy.auth import OAuthHandler
import os
import re
import string

class Tweeterpy:

    ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    CONSUMER_KEY = os.environ.get('CONSUMER_TWITTER_KEY')
    CONSUMER_SECRET_KEY = os.environ.get('CONSUMER_SECRET_TWITTER_KEY')

    def __init__(self, tweets = tweepy,
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY),
        ACCESS_TOKEN = ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
    ):
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
        self.tweets = tweepy

    def strip_links(self, text):
        link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
        links         = re.findall(link_regex, text)
        for link in links:
            text = text.replace(link[0], '')
        return text

    def strip_all_entities(self, text):
        entity_prefixes = ['@','#']
        words = []
        for word in text.split():
            word = word.strip() #removes whitespace
            if word:
                if word[0] not in entity_prefixes:
                    words.append(word)
        return ' '.join(words)

    def strip_rt(self, text):
        return text.replace('RT', '')

    def format_output(self, text):
        return self.strip_all_entities(self.strip_links(self.strip_rt(text)))

    def get_tweets(self, text):
        result = self.tweets.Cursor(self.api.search, q=text, geocode="51.5074,0.1278,20km", lang='en',rpp='100',result_type='recent').items(100)
        raw_output = ''
        for tweet in result:
            raw_output += " " + tweet.text
        output = self.format_output(raw_output)
        return output
