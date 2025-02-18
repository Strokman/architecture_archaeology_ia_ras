from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    """
    Заготовка для главной страницы.
    Может быть будут какие-то новости или еще что-то подобное
    """
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'title': 'Домашняя страница'}, request))
