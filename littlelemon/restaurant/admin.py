from django.contrib import admin
from .models import Booking, Menu
# from rest_framework.authtoken.models import Token


# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
# admin.site.register(Token)