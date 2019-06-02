from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

def index(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "index.html", {"greetings": greetings})
