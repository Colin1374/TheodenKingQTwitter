import tweepy
import config
import random


#make a config.py file in the same directory, put your keys in that file
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = config.access_token
access_token_secret = config.access_token_secret
auth.set_access_token(access_token, access_token_secret)

#change this directory here to match yours
s = open('/Users/colin.hughes/Documents/TheodenKing/theodenlines.txt', 'r')
m = s.readlines()
l = []
for i in range(0,len(m) -1):
    x = m[i]
    z = len(x)
    a = x[:z - 1]
    l.append(a)
l.append(m[i + 1])
o = random.choice(l)
s.close()

api = tweepy.API(auth)
res = api.update_status(o)
