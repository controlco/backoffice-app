from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import Report, User
# Create your tests here.


class ReportTests(APITestCase):
    def test_create_report(self):
        """
        Ensure we can create a new report object.
        """
        from_report = User.objects.create(username='user@uc.cl', id=1)
        to_report = User.objects.create(username='user2@uc.cl', id=2)
        data = {'title': 'Denuncia',
                'content': "Denuncia de prueba", "owner": from_report.id, "reported_user": to_report.id}
        response = self.client.post("/reports/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Report.objects.count(), 1)
        self.assertEqual(response.data["title"], 'Denuncia')
