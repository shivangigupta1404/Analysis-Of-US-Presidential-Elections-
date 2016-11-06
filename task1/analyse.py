import io,re
import pymongo
from time import sleep
from pymongo import MongoClient
client=MongoClient()
db=client.final
#For geocodding
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from .models import marker,hashtag,retweet,favorite
#custom script
from text_processor import *

def tweetsVSretweets():
    try:
        retweet.objects.all().delete()
        retwit=0
        tweet=0
        for data in db.tweets.find():
            if data['retweeted'] or 'RT @'  in data['text']:
                retwit=retwit+1
            else:
                tweet=tweet+1
        a=retweet()
        a.category="Tweets"
        a.count=tweet
        a.save()

        b=retweet()
        b.category="Retweets"
        b.count=retwit
        b.save()
    except Exception as e:
        print e

def TopHashTags():
    try:
        hashtag.objects.all().delete()
        query=db.tweets.aggregate([{"$sort":{"_id":-1}}, {"$match": {"entities.hashtags.text":{"$exists":True}}},{"$unwind":"$entities.hashtags"}, {"$project" : {"entities.hashtags.text":1,"_id":0}}, {"$group":{"_id":{"$toLower":"$entities.hashtags.text"}, "count" : {"$sum" : 1 }}}, {"$sort":{"count":-1}}, {"$limit":10}])
        for data in query:
            tag=data['_id'].encode('utf-8',errors='ignore')
            freq=data['count']
            a=hashtag()
            a.hashtag=tag
            a.count=freq
            a.save()
    except Exception as e:
        print e

def favCount():
    try:
        favorite.objects.all().delete()
        query=query= db.tweets.aggregate([{"$match":{'text':{"$regex":re.compile("^RT @.*")}}},{"$group":{'_id':'$retweeted_status.favorite_count','count':{"$sum":1}}},{"$sort":{'_id':-1}}])
        for data in query:
            a=favorite()
            a.value=data['_id']
            a.count=data['count']
            a.save()
    except Exception as e:
        print e

def tweetLocations():
    count=1
    try:
        marker.objects.all().delete()
        for data in db.tweets.find({"$or":[{'coordinates':{"$ne":None}},{'place':{"$ne":None}}]}):
            text=preprocess_str(clean(data['text']))
            if data['coordinates']: #When tweeting from phone   
                latitude=data['coordinates']['coordinates'][0]
                longitude=data['coordinates']['coordinates'][1]
                type="coordinate"
            elif data['place']: #When tweeting from Desktop
                #To find a single cordinate instead of box as present in data['place']['cordinates']
                location = geolocator.geocode(data['place']['country'],timeout=10) 
                latitude =location.latitude
                longitude=location.longitude
                type="place"
                sleep(1)

            a=marker()
            a.user_name    =data['user']['screen_name']
            a.markerName   =text
            a.marker_type  =type
            a.longitude    =longitude
            a.latitude     =latitude 
            a.save()
            print count
            count=count+1
    except Exception as e:
        print "problem : ",e.message

