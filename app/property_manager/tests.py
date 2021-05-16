# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from property_manager.models import Region, District, Property
from accounts.models import User
from property_manager.serializers import RegionSerializer
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


class PropertyTests(APITestCase):
    def setUp(self):
        self.data = {"email": "test@gmail.com", "password": "123",
                     "first_name": "Test Name", "last_name": "Test LastName", "is_active": True}

        self.client.post(
            "/signup/", self.data, format="json"
        )
        data = {"email": self.data["email"], "password": self.data["password"]}
        self.token = self.client.post(
            "/login/", data, format="json").data["token"]
        self.user = User.objects.get(email=self.data["email"])

        self.title = "Propiedad"
        self.district = 1
        self.region = Region.objects.create(name='RM', number=13)
        self.district = District.objects.create(
            name="Providencia", id=1, region=self.region)

    def admin_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_property(self):
        """
        Ensure we can create a new property object.
        """
        self.admin_authentication()
        data = {"title": self.title, "district": self.district.id}
        response = self.client.post("/properties/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
