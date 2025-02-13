from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        # adds a new instance of the Menu model
        item = Menu.objects.create(id='10', title="IceCream", price=80, inventory=100)
        # anticipated value
        self.assertEqual(str(item), "IceCream : 80")