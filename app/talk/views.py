from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Here is the about page. www.liangz.org")


def about(request):
    return HttpResponse("Here is the about page. www.liangz.org")

