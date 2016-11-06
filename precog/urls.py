from django.conf.urls import url
from django.contrib import admin
from task1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^map/$',views.map,name='map'),
    url(r'^1/$',views.graph1,name='graph1'),
    url(r'^2/$',views.graph2,name='graph2'),
    url(r'^4/$',views.graph4,name='graph4'),
    url(r'^analysis/$',views.calculate,name='analysis'),
]
