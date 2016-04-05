import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'V1BfuqPf0FVwSt04pmyvGbgZK'
consumer_secret = 'BAcpMibqOHXpn3agrKksh1sP10kpJNSMDzSXKmx4LgY7L0oc0v'
access_token = '713909144344854528-eawB9qOiNgtt2gsjwBY8L7EPeR15GsN'
access_secret = 'v2sVvCM5Y1qn3ITRFp31h7WB9ng7vFU2PYdIXhlhIYWPU'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)