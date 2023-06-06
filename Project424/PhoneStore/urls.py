from django.urls import path
from . import views

app_name = 'PhoneStore'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:phone_id>", views.add, name='add'),
    path("list", views.phone,name='phone'),
    path("update/<int:phone_id>", views.Update, name='update'),
    path('logina', views.logina, name='login'),
    path('register/', views.register, name="register"),
    path('addProduct', views.viewaddform, name='viewaddform')

]