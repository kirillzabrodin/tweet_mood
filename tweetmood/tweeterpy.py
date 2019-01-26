import json
import tweepy
from tweepy.auth import OAuthHandler
import os
import re
import string

class Tweeterpy:

    def __init__(self):
        auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_TWITTER_KEY'), os.environ.get('CONSUMER_SECRET_TWITTER_KEY'))
        auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'), os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))
        self.api = tweepy.API(auth)

    def strip_links(text):
        link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
        links         = re.findall(link_regex, text)
        for link in links:
            text = text.replace(link[0], ', ')
        return text

    def strip_all_entities(text):
        entity_prefixes = ['@','#']
        for separator in  string.punctuation:
            if separator not in entity_prefixes :
                text = text.replace(separator,' ')
        words = []
        for word in text.split():
            word = word.strip()
            if word:
                if word[0] not in entity_prefixes:
                    words.append(word)
        return ' '.join(words)

    def format_output(text):
        return Tweeterpy.strip_all_entities(Tweeterpy.strip_links(text))

    def get_tweets(self, text):
        result = tweepy.Cursor(self.api.search, q=text, geocode="51.5074,0.1278,20km", lang='en',rpp='10',result_type='recent').items(10)
        raw_output = ''
        for tweet in result:
            raw_output += " " + tweet.text
        output = Tweeterpy.format_output(raw_output).replace('RT', '')
        return output
