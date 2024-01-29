from django.http import HttpResponse
from django.template import loader
from django.views import View
from decimal import Decimal


class IndexView(View):
    pass


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    a = Decimal('123.31232')
    print(a)
    context = {
        'text': 'placeholder'
    }
    return HttpResponse(template.render(context, request))
