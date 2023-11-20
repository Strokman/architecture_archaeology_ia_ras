from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.core.handlers.wsgi import WSGIRequest as req
from helpers.models import Preservation, Comment
import architecture_archaeology.settings as settings
from logging import getLogger
import pprint


logger = getLogger(f'{settings.PROJECT}.{__name__}')


# Create your views here.
def index(request: req):
    # pprint.pprint(request.__dict__)
    logger.info('test msg')
    template = loader.get_template('artworks/index.html')
    p = Preservation(description='asdsaasd')
    p.save()
    c = Comment(text='text message')
    c.save()
    return HttpResponse(template.render({1: 'lol'}, request))


def add_artwork(request, id):
    return HttpResponse('Test ' + str(id))