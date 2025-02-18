from django.db import models

# Create your models here.
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

    
    