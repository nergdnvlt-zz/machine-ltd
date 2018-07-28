from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
