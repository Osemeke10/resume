from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(label = 'E-mail')
    message = models.CharField(required = False)
    phone = models.CharField