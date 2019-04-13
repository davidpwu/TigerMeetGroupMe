from django.urls import path, re_path

from .views import index, about, gmlogin, createchat, joinchat, events, todo, add

urlpatterns = [
    path('', gmlogin, name='gmlogin'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    re_path(r'^join/(?P<group_name>[^/]+)', joinchat, name='joinchat'),
    re_path(r'^category/(?P<group_name>[^/]+)', events, name='events'),
    # This is the url re for making any chat
    re_path(r'^makechat/(?P<group_name>[^/]+)', createchat, name='createchat'),

    path('todo/', todo, name='todo'),
    re_path(r'^add', add, name='add')
]