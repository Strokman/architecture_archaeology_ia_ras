from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView

from django.core.handlers.wsgi import WSGIRequest as req
from helpers.models import Preservation, Comment
import architecture_archaeology.settings as settings
from logging import getLogger
import pprint


logger = getLogger(f'{settings.PROJECT}.{__name__}')


# Create your views here.
class IndexView(TemplateView):
    template_name = 'artworks/index.html'

    async def get(self, request: req):
        # pprint.pprint(request.__dict__)
        logger.info('test')
        # p = Preservation(description='asdsaasd')
        # await p.asave()
        # c = Comment(text='text message')
        # await c.asave()
        return render(request, self.template_name, {1: 'lol'})

    # async def add_artwork(self, request, id):
    #     return HttpResponse('Test ' + str(id))
