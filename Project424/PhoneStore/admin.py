from django.contrib import admin
from .models import  MyUser,Phone

# Register your models here.

admin.site.register(Phone)
# admin.site.register(Cart)
admin.site.register(MyUser)