from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
    url(r'^$','account.views.loginView',name = "login"),
    url(r'^logout/$','account.views.logoutView' ,name="logout"),
    url(r'^home/$', 'account.views.home',name="home"),
    
   
] 
