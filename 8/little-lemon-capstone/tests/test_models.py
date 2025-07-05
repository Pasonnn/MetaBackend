from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_str_method(self):
        item = Menu.objects.create(title="Ice Cream", price=5.99, inventory=10)
        self.assertEqual(str(item), "Ice Cream")