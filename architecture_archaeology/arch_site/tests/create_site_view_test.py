from django.urls import reverse

from arch_site.models import ArchaeologicalSite
from arch_site.forms import SubmitArchaeologicalSiteForm
from core.tests import BaseTestCreateView


class CreateSiteViewTest(BaseTestCreateView):
    fixtures = ['countries.json',
                'regions.json'
                ]
    model = ArchaeologicalSite
    form = SubmitArchaeologicalSiteForm
    
    def setUp(self):
        self.url = reverse('arch_site:submit')
        self.payload = {
            'name': "Килиса-кая",
            'long': 56.6,
            'lat': 45.3,
            'region': 16
        }
