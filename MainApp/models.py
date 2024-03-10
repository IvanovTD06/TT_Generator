from django.db import models


class user_registration(models.Model):
    
    Username = models.CharField(max_length=64)
    Password = models.CharField(max_length=64)
    