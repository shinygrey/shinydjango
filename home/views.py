from django.shortcuts import render
from django.http import HttpResponse

from .models import Experiments

def index(request):

    test1 = Experiments("4")
	firstName = test1["data"]["first_name"]
    currentTime = test1.datetime1
	

    return render(request, "index.html", {"greetings": currentTime, "restdata": test1.firstName})
