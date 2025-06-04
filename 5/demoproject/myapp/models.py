from django.db import models

# Create your models here.
class Drink(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.drink_name} : {self.price}"

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.guest_count}"
    
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.role} : {self.shift}"
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} : {self.price}"