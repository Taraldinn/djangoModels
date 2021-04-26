from django.shortcuts import render
from django.http import HttpResponse

from appone.models import Musician, Album

# Create your views here.


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction ={'text_1': 'this is list of musicians, ', 'musician' : musician_list }
    return render(request, 'first_app/index.html', context=diction)
    # return HttpResponse("<h1>I am from here</h1>")


