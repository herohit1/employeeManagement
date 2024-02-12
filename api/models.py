from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name
