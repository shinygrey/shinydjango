from django.shortcuts import render
from django.http import HttpResponse

from .models import Experiments

def index(request):

    test1 = Experiments()

    greetings = test1.datetime1 + " " + test1.responsedata
	

    return render(request, "index.html", {"greetings": greetings})
