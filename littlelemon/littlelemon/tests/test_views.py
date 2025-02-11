from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = Menu.objects.create(id='1', title="lemon cake", price=12.99, inventory=10)
        self.menu2 = Menu.objects.create(id='2', title="lemon pizza", price=17, inventory=8)
        self.menu3 = Menu.objects.create(id='3', title="lemon ice cream", price=4, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)