from rest_framework.test import APITestCase
from rest_framework import status
from chat.models import Message
from accounts.models import User


# Create your tests here.
class MessageTests(APITestCase):

    def setUp(self):
        # Create & login user 1: sender
        self.data_user_1 = {"email": "test_message_1@gmail.com", "password": "123",
                     "first_name": "Test Name message 1", "last_name": "Test LastName", "is_active": True}
        self.client.post("/signup", self.data_user_1, format="json")
        self.token_user_1 = self.client.post(
            "/login", self.data_user_1, format="json").data["token"]
        self.user_1 = User.objects.get(email=self.data_user_1["email"])
        
        # Create user 2: recipient
        self.data_user_2 = {"email": "test_message_2@gmail.com", "password": "123",
                    "first_name": "Test Name message 2", "last_name": "Test LastName", "is_active": True}
        self.client.post("/signup", self.data_user_2, format="json")
        self.user_2 = User.objects.get(email=self.data_user_2["email"])

    
    def admin_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_user_1)


    def test_create_message(self):
        """
        Ensure we can create a new message object.
        """
        data_message = {"subject": "Mensaje prueba", "content": "Probando 1, 2, 3", 
        "from_user": self.user_1.id, "to_user": self.user_2.id}
        self.admin_authentication()
        response = self.client.post("/users/{}/messages/".format(self.user_1.id), data_message, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(response.data["subject"], 'Mensaje prueba')

    
