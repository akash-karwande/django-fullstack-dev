from django.http import HttpResponse;
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello from home page")
    return render(request, "website/index.html")


def about(requst):
    return HttpResponse("Hello from about page")

def contact(request):
    return HttpResponse("hello from contact page")