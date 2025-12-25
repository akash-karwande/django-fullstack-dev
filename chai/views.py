from django.shortcuts import render
from .models import ChaiVarities

# Create your views here.

def all_chai(request):
    chais = ChaiVarities.objects.all()
    return render(request, 'chai/index.html', {'chais': chais})


def order_chai(request):
    return "Order chai page"
