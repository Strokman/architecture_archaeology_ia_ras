from django.test import TestCase, Client
from django.urls import reverse

from building.models import Building
from arch_site.models import ArchaeologicalSite


class CreateBuildingViewTest(TestCase):
    client = Client()
    fixtures = ['countries.json', 'regions.json', 'arch_sites.json', ]

    def test_form_valid(self):
        form = self.form(data=self.building)
        self.assertTrue(form.is_valid())

    # def test_building_created(self):
    #     req = self.client.post(reverse('building:submit'), data=self.building, follow=True)
    #     req = RequestFactory().post(reverse('building:submit'), data=self.building)
    #     # self.assertEqual(resp.status_code, 301)
    #     resp = SubmitBuildingView.as_view()(req)
    #     print(resp)
    #     self.assertRedirects(resp, "/")
        # self.assertEqual(len(Building.objects.all()), 1) #self.building['name'])

    # def test_building_created(self):
    #     self.model = Building.objects.create(name='Test name', description='test desc', long=12, lat=13)
    #     resp = self.client.get(reverse('building:display'))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.context['building'], self.model)