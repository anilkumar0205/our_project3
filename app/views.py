from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('<marquee><h1>hi jampandu how are you</h1></marquee>')
def king(request):
    return HttpResponse('<marquee><h1>king of the forest is lion</h1></marquee>')