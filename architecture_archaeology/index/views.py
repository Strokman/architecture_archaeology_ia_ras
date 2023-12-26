from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View



class IndexView(View):
    pass


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'text': 'placeholder'
    }
    return HttpResponse(template.render(context, request))
