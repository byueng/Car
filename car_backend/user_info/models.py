from django.db import models
from cars.models import CarInfo

class User(models.Model):
    account = models.CharField(
        max_length = 12,
        help_text = "user identify, max length: 12",
        primary_key = True,
        )

    password = models.CharField(
        max_length = 50,
        help_text = "Login user name",
        null = True,   
        )
    
    def __str__(self):
        return self.account


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.account


class FavoriteCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_cars")
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE, default=12)  # Set default value
    car_details = models.TextField(help_text="Details of the car", blank=True, null=True)

    def __str__(self):
        return f"{self.user.account} - {self.car.brand}:{self.car.model} {self.car.price}万元"