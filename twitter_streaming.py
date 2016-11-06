from twython import Twython, TwythonError, TwythonStreamer
import json
import pymongo

from pymongo import MongoClient
client=MongoClient()
db=client.final

#This is your Twitter application details
APP_KEY = 'Gfwfp7CxswWBMMlATKXjmkPIC'
APP_SECRET = 'W3hrXUJZkCe5weC6NiJ2ZVBEfbekvdjcgY7Wy4FVKso8SknXok'
OAUTH_TOKEN = '2199166969-jlgySnQsssOiOAT77zCe7DGDJvFitbE9Qg6KScw'
OAUTH_TOKEN_SECRET = 'w060EZrimKlh0zyMDFWalmC0kQVIglbqnKo4OU5eKfeOy'

class MyStreamer(TwythonStreamer):
        def on_success(self, data):
                try:
                        result_text=data['text'].encode('utf-8')
                        print data['created_at'] , result_text 
                        db.tweets.insert(data)
                except Exception as e:
                        print "problem ",e
                        
        def on_error(self, status_code, data):
                print status_code,data

keywords=['#USelections','#clinton', '#trump']
stream = MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
stream.statuses.filter(track=keywords)
