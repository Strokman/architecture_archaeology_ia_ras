from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('artworks/index.html')
    return HttpResponse(template.render({1: 'lol'}, request))


def add_artwork(request, id):
    return HttpResponse('Test ' + str(id))