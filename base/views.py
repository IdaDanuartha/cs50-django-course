import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def about(request):
    return HttpResponse("Hi, its me danu!")

def profile(request, name):
    return render(request, "home/profile.html", {
        "name": name.capitalize()
    })

def newyear(request):
    is_newyear = datetime.datetime.now()
    return render(request, "home/newyear.html", {
        "is_newyear": is_newyear.month == 1 and is_newyear.day == 1
    })