from django.shortcuts import render
from .models import Product,ProductCategory
from django.db.models import Avg, Min, Max

# Create your views here.


def products_detail(request, product_slug):
    product_detail = Product.objects.get(slug=product_slug)
    return render(request, "product_module/products_details.html", {'product_detail': product_detail})


def products_list(request):

    products = Product.objects.all().order_by("-price")
    number_of_products = products.count()
    return render(request, "product_module/products_list.html", {'products': products, 'number_of_products' : number_of_products})
