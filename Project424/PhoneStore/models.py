from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Phone(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()


def str(self):
    return f"{self.id} {self.name} {self.price} {self.manufacturer} {self.description}"


class MyUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    # cart = models.ManyToManyField(Phone,blank=true,related_name=cart)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class Cart(models.Model):
#     username = models.ManyToManyRel(MyUser())
#     item = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="item")
#     quantity = models.IntegerField()
