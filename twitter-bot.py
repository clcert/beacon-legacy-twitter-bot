import tweepy
import time
import json


config = json.load(open("tokens.json"))['twitter']
auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_token"], config["access_token_secret"])
api = tweepy.API(auth)

TWEET = 'This is a test tweet'

api.update_status(TWEET)
