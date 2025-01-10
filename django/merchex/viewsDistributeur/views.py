from django.shortcuts import render
from django.http import HttpResponse

def distri(request):
    return HttpResponse('views du distributeur')