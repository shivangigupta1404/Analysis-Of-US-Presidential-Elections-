from django.contrib import admin
from .models import *

# Register your models here.
class markerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'markerName' , 'marker_type' ,'longitude','latitude')
admin.site.register(marker, markerAdmin)

class hashtagAdmin(admin.ModelAdmin):
    list_display = ('hashtag', 'count')
admin.site.register(hashtag, hashtagAdmin)

class retweetAdmin(admin.ModelAdmin):
    list_display = ('category', 'count')
admin.site.register(retweet, retweetAdmin)

class favoriteAdmin(admin.ModelAdmin):
    list_display = ('value', 'count')
admin.site.register(favorite, favoriteAdmin)