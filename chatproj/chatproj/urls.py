from django.conf.urls import url, include
from chatapp import views
from chatapp.views import index, chat, send, prodone, prodtwo, prodthree


urlpatterns = [
    url(r'^view_users/$', views.view_users),
    url(r'^save_msg/$', views.save_msg),
    url(r'^get_chat/$', views.get_chat),
    url(r'^view_msg/$', views.view_msg),
    url(r'^index', index, name='index'),
    url(r'^chat', chat, name='chat'),
    url(r'^send', send, name='send'),
    url(r'^prodone', prodone, name='prodone'),
    url(r'^prodtwo', prodtwo, name='prodtwo'),
    url(r'^prodthree', prodthree, name='prodthree'),
]
