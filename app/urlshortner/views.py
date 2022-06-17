from django.http import HttpResponse
from django.shortcuts import redirect, render
import uuid
from .models import *


def index(request):
    return render(request, 'urlshortner/index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']  # name of input tag
        uid = str(uuid.uuid4())[:5]
        Url.objects.create(link=link, uuid=uid)
        return HttpResponse(uid)  # send to ajax


def go(request, pk):
    url_object = Url.objects.get(uuid=pk)
    return redirect(url_object.link)
