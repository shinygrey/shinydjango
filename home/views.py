from django.shortcuts import render
from django.http import HttpResponse

from .models import Experiments
from .models import Xkcd

def index(request):
	test1 = Experiments("4")
	firstName = test1.data["data"]["first_name"]
	category_list = ["apple","grape","banana"]
	dictionarytest = {"data": {"first_name": "Helen"}}
	testName = dictionarytest["data"]["first_name"]
	currentTime = test1.datetime1
	return render(request, "index.html", {"greetings": currentTime, "test": testName, "restdata": firstName, "category_list": category_list})

def xkcd(request):
	comic = Xkcd(2134)
	return render(request, "index.html", {"greetings": "greetings here", "test": "test here", "restdata": comic.data["img"]})
