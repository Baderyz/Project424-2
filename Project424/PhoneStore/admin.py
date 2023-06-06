from django.contrib import admin
from .models import Phone, MyUser

# Register your models here.

admin.site.register(Phone)
# admin.site.register(Cart)
admin.site.register(MyUser)