# from django.db import models

# # Create your models here.

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     image = models.ImageField(upload_to='user_images/', null=True, blank=True)
#     firstName = models.CharField(max_length=255)
#     lastName = models.CharField(max_length=255)
#     phoneNumber = models.CharField(max_length=15)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)