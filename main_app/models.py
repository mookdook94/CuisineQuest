from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})
