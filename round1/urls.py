__author__ = 'Zachary'
from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('round1.views',
    url(r'^frontpage', 'frontpage', name='frontpage'),
    url(r'^viewfolder', 'viewfolder', name='viewfolder'),
    url(r'^index', 'home',name='home'),
    url(r'^$', 'home',name='home'),
    url(r'^about', 'about',name='about'),
    url(r'^rules','rules',name='rules'),
    url(r'submit','submit',name='submit'),
    url(r'register','register',name='register'),
    url(r'login','user_login',name='user_login'),
    url(r'logout','user_logout',name='user_logout'),
    url(r'list','list',name='list')
#    url(r'^admin', 'admin', name='admin')
    )
