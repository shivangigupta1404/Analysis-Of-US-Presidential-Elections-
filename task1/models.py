from django.db import models

class marker(models.Model):
	user_name  = models.CharField(max_length=250)
	markerName= models.CharField(max_length=1250, default=None,null=True)
	marker_type = models.CharField(max_length=50, default=None,null=True)
	longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True)
	latitude = models.DecimalField(max_digits=11, decimal_places=8, null=True)

class hashtag(models.Model):
	hashtag=models.CharField(max_length=250)
	count=models.IntegerField()

class retweet(models.Model):
	category=models.CharField(max_length=250)
	count=models.IntegerField()

class favorite(models.Model):
	value=models.IntegerField()
	count=models.IntegerField()
