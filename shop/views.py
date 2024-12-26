from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def ProductList(request):
    context  = {
        'product':Product.objects.all()
    }
    return render(request,'shop/product.html',context)

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at Contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at Checkout")