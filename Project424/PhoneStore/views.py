from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Phone
from PhoneStore.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return reverse()
    else:
        form = SignUpForm()

    return render(request, 'PhoneStore/register.html', {'form': form})


def logina(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # replace 'home'with the name of your home page URL pattern
            return redirect('home')
        else:
            # handle invalid login credentials
            pass
    else:
        return render(request, 'PhoneStore/login.html')


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


def add(request,phone_id):
    phone = Phone.objects.get(id = phone_id)
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
#