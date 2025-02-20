from django.db import models

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

    