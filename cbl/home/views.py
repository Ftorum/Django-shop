from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category, Product

# Create your views here.

def index(request):
    category = Category.objects.all()
    products_cold = Product.objects.all().order_by('category')
    context = {'category':category,'products_cold':products_cold}
    return render(request,'home/home.html',context)

def category_products(request,id,slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context={'products':products,'category':category}
    return render(request,'home/category_products.html', context)

def product_datail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    context={'product':product,'category':category}
    return render(request,'home/product_datail.html', context)



