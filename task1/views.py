from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, Template
#custom scripts
from analyse import *
import io

def index(request):
	h=hashtag.objects.all().order_by('-count')[:5]
	r=retweet.objects.all()
	template= loader.get_template('task1/index.html')
	return HttpResponse(template.render({'hashtag':h,'retweet':r,},request))

def graph1(request):
	r=retweet.objects.all()
	template= loader.get_template('task1/1.html')
	return HttpResponse(template.render({'retweet':r,},request))

def graph2(request):
	h=hashtag.objects.all()
	template= loader.get_template('task1/2.html')
	return HttpResponse(template.render({'hashtag':h,},request))

def map(request):
	m=marker.objects.all()
	template= loader.get_template('task1/map.html')
	return HttpResponse(template.render({'marker':m,},request))

def graph4(request):
	f=favorite.objects.all().order_by('value')
	template= loader.get_template('task1/4.html')
	return HttpResponse(template.render({'favorite':f,},request))

def calculate(request):
	tweetsVSretweets()
	print "tweet vs retweet done"
	TopHashTags()
	print "Top hashtag calculated"
	favCount()
	print "favorite count calculated"
	tweetLocations()
	print "locations calculated"
	HttpResponse=index(request)
	return HttpResponse
