from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
# Create your views here.
def hello(request):
	return HttpResponse('Hey Wassup!');

def follow(request):
	follower_id = request.GET['id1']
	following_id = request.GET['id2']
	try:
		follower = Profile.objects.get(pk = follower_id)
	except:
		follower = Profile.objects.create(account = user,city = City.objects.get(id=1),street_address = "dsad")
	follower.following.add(User.objects.get(id= following_id))

def getallusers(request):
	data = serializers.serialize('json',User.objects.all())
	return HttpResponse(data,content_type = "application/json")	
