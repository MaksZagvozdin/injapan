from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    name = "Maks"
    current_day = "11.11.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())

def contacts(request):
    return render(request, 'contacts.html', locals())

def about(request):
    return render(request, 'about.html', locals())
def company(request):
    return render(request, 'company.html', locals())
def zakazavto(request):
    return render(request, 'zakazavto.html', locals())
def pravila(request):
    return render(request, 'pravila.html', locals())
def calculator(request):
    return render(request, 'calculator.html', locals())
def dostavca(request):
    return render(request, 'dostavca.html', locals())