from django.contrib import admin
from .models import Drink, Booking, Employee, Menu

# Register your models here.
admin.site.register(Drink)
admin.site.register(Booking)
admin.site.register(Employee)
admin.site.register(Menu)