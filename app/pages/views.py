from django.shortcuts import render, get_object_or_404
from .models import Good

def index(request):
    goods = {
        "items":Good.objects.all()
    }
    return render(request, 'pages/index.html', goods)

def products(request):
    return render(request, 'pages/products.html')

def special_offer(request):
    return render(request, 'pages/special_offer.html')

def product(request, product_id):
    product = get_object_or_404(Good, pk=product_id)
    context = {'product': product}
    return render(request, 'pages/product_details.html', context=context)

def compair(request):
    return render(request, 'pages/compair.html')

def summary(request):
    return render(request, 'pages/product_summary.html')

def login(request):
    return render(request, 'pages/login.html')

def forgetpass(request):
    return render(request, 'pages/forgetpass.html')

def register(request):
    return render(request, 'pages/register.html')

def contact(request):
    return render(request, 'pages/contact.html')

def normalinfo(request):
    return render(request, 'pages/normal.html')

def faq(request):
    return render(request, 'pages/faq.html')