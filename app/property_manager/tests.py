# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from property_manager.models import Region, District
# Create your tests here.


class RegionTests(APITestCase):
    def test_create_region(self):
        """
        Ensure we can create a new region object.
        """
        data = {'name': 'RM', 'number': 13}
        actual_number = Region.objects.count()
        response = self.client.post("/regions/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Region.objects.count(), actual_number + 1)
        self.assertEqual(response.data["name"], 'RM')


class DistrictTests(APITestCase):
    def test_create_district(self):
        """
        Ensure we can create a new district object.
        """
        region = Region.objects.create(name='RM', number=13)
        data = {'name': 'Providencia', 'region': 13}
        response = self.client.post("/districts/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(District.objects.count(), 1)
        self.assertEqual(response.data["name"], 'Providencia')
