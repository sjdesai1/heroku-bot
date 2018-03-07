# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "I0LfuIedY1eMqV4xyZUo2el4a"
consumer_secret = "ELrlMPMz7uqeXHWoxNU1j93fVhSpLgJVWn8srwirwIbxQnbaDm"
access_token = "925121288196071424-jWWOLljGIs3z2aFtXpOaqPHZ7Tn3uSC"
access_token_secret = "pxm9uxAd2mCorAxlXiyM29vOVPzV03oJsG19SftqJJLVK"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE