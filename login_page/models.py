# login_page/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.username