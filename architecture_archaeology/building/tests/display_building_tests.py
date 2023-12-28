from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from building.models import Building
from building.forms import SubmitBuildingForm
from building.views import SubmitBuildingView
from arch_site.models import ArchaeologicalSite


class DisplayBuildingViewTest(TestCase):
    client = Client()
    fixtures = ['countries.json', 'regions.json', 'arch_sites.json']

    def setUp(self):
        self.form = SubmitBuildingForm
        self.building = {
        'name': 'Церковь Покрова не Нерли',
        'long': 55.9,
        'lat': 60.88,
        'description': 'test-description',
        'site': ArchaeologicalSite.objects.last()
    }

    # def test_no_building(self):
    #     resp = self.client.get(reverse('building:display', kwargs={'slug': 'test'}))
    #     print(resp)
    #     self.assertEqual(resp.status_code, 404)
        
    def test_url(self):
        resp = self.client.get(reverse('building:submit'))
        self.assertEqual(resp.status_code, 200)

    # def test_form_valid(self):
    #     form = self.form(data=self.building)
    #     self.assertTrue(form.is_valid())

    def test_building_created(self):
        req = self.client.post(reverse('building:submit'), data=self.building, follow=True)
        req = RequestFactory().post(reverse('building:submit'), data=self.building)
        # self.assertEqual(resp.status_code, 301)
        resp = SubmitBuildingView.as_view()(req)
        print(resp)
        self.assertRedirects(resp, "/")
        # self.assertEqual(len(Building.objects.all()), 1) #self.building['name'])

    # def test_building_created(self):
    #     self.model = Building.objects.create(name='Test name', description='test desc', long=12, lat=13)
    #     resp = self.client.get(reverse('building:display'))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.context['building'], self.model)

