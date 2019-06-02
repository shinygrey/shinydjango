from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

def index(request):

    greeting = Greeting()

    greetings = Greeting.datetime1

    return render(request, "index.html", {"greetings": greetings})
