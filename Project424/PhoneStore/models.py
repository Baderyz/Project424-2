
from django.db import models
from django.contrib.auth.models import User


class Phone(models.Model):
    
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
   

def str(self):
    return f"{self.id} {self.name} {self.price} {self.manufacturer} {self.description}"


class Cart(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Phone,on_delete=models.CASCADE,related_name="item")
    quantity = models.IntegerField(max_length=2)


