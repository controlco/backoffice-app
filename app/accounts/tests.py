from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import Report, User
# Create your tests here.


class UserTests(APITestCase):

    def setUp(self):
        self.data = {"email": "test@gmail.com", "password": "123",
                     "first_name": "Test Name", "last_name": "Test LastName", "is_active": True}

    def admin_authentication(self, token):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_signup(self):

        response = self.client.post(
            "/signup/", self.data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        self.client.post(
            "/signup/", self.data, format="json"
        )
        data = {"email": self.data["email"], "password": self.data["password"]}
        response = self.client.post("/login/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        self.client.post(
            "/signup/", self.data, format="json"
        )
        data = {"email": self.data["email"], "password": self.data["password"]}
        token = self.client.post("/login/", data, format="json").data["token"]
        self.admin_authentication(token)
        user = User.objects.get(email=self.data["email"])
        data = {"email": "new@gmail.com"}
        response = self.client.patch(f"/users/{user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReportTests(APITestCase):
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

    def admin_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_report(self):
        """
        Ensure we can create a new report object.
        """
        to_report = User.objects.create_superuser(
            email='user2@uc.cl', password="123")
        data = {'title': 'Denuncia',
                'content': "Denuncia de prueba", "owner": self.user.id, "reported_user": to_report.id}
        self.admin_authentication()
        response = self.client.post("/reports/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Report.objects.count(), 1)
        self.assertEqual(response.data["title"], 'Denuncia')
