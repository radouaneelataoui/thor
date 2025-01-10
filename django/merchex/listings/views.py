from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello les gens")

def about(request):
    return HttpResponse("about - us")

def m2i(request):
    return HttpResponse('promo 2024')

# Create your views here.
