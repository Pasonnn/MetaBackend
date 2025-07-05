from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)  # Authenticate the client
        self.item1 = Menu.objects.create(title="Pizza", price=10.99, inventory=5)
        self.item2 = Menu.objects.create(title="Burger", price=8.99, inventory=10)
        self.url = reverse('menu-items')  # Adjust to your actual URL name

    def test_getall(self):
        response = self.client.get(self.url)
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)