from logging import getLogger
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest as req
import architecture_archaeology.settings as settings
from building.models import Building

logger = getLogger(f'{settings.PROJECT}.{__name__}')


class Display(DetailView):
    model = Building
    template_name = 'building/display.html'

    def get(self, request: req):
        # pprint.pprint(request.__dict__)
        logger.info('test')
        # building = 'TEST DATA'
        building = get_object_or_404(Building)
        # p = Preservation(description='asdsaasd')
        # await p.asave()
        # c = Comment(text='text message')
        # await c.asave()
        return render(request, self.template_name, {'building': building})