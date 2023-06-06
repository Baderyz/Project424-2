from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import  MyUser,Phone
from .forms import ItemForm


# from .forms import SignUpForm


# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             return login(username,password)
#     else:
#         form = SignUpForm()
#
#     return render(request, 'PhoneStore/register.html', {'form': form})


def phone(request):
    return render(request, 'PhoneStore/allProducts.html', {
        'phone': Phone.objects.all()
    })


class NewItemForm(forms.Form):
    item = forms.IntegerField(label='Number of items')


def index(request):
    if "PhoneStore" not in request.session:
        request.session["PhoneStore"] = []

    return render(request, "PhoneStore/index.html", {"PhoneStore": request.session["PhoneStore"]})


def add(request, phone_id):
    if request.method == 'POST':
     username = request.user.username
     phone = Phone.objects.get(id=phone_id)
     user = MyUser.objects.get(username=username)
     user.cart.add(phone)
     
     
    phone = Phone.objects.get(id=phone_id)
    username = request.user.username
    user = MyUser.objects.get(username=username)
    if request.user.is_authenticated:
        user.cart.add(phone)
    else:
        pass
    return render(request, 'PhoneStore/specificProduct.html', {
        'phone': phone
    })


# user add new product


class uaddproductForm(forms.ModelForm):
    class Meta:
        model = Phone
        # fields = ['name', 'manufacturer', 'price', 'description']
        fields = "__all__"

def viewaddform(request):
    if request.method == 'POST':

        form = uaddproductForm(request.POST)
        if (form.is_valid()):
            form.save()

    else:
        form = uaddproductForm()

    return render(request, "PhoneStore/userAddP.html",
                  {"form": uaddproductForm()})


from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm


# class RegisterView(CreateView):
#     form_class = MyUserCreationForm
#
#     def form_valid(self, form):
#         form.save()
#         return redirect('home')
def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('PhoneStore:login'))
    else:
        form = MyUserCreationForm()

    return render(request, 'PhoneStore/register.html', {'form': form})





#
def logina(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # replace 'home'with the name of your home page URL pattern
            # url = reverse('PhoneStore/register')
            return redirect(reverse("PhoneStore:phone"))
        else:
            # handle invalid login credentials
            return redirect(reverse("PhoneStore:logina"))
            pass
    else:
        return render(request, 'PhoneStore/login.html')
    


def Update(request , phone_id):
    phone = Phone.objects.get(id = phone_id)
    form = ItemForm(request.POST or None,instance=phone)
    if form.is_valid():
        form.save()

    return render(request, "PhoneStore/update.html",
                  {'phone':phone,
                   'form':form})   
