from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'urlshortner/index.html')


def create(request):
    return HttpResponse('Createpage')
