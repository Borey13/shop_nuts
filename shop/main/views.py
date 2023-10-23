import random
from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Product
from cart.forms import CartAddProductForm


def main(request):
    data = Category.objects.all()
    products = Product.objects.all()
    popular_product = random.sample(list(products), 6)
    return render(request, 'main/main.html', {'categories': data, 'popular': popular_product})


def about(request):
    products = Product.objects.all()
    popular_product = random.sample(list(products), 6)
    return render(request, 'main/about.html', {'popular': popular_product})


def category(request, id_cat):
    products = Product.objects.all()
    data = products.filter(category_id=id_cat)
    popular_product = random.sample(list(products), 6)
    cat_name = Category.objects.get(category_id=id_cat)
    return render(request, 'main/category.html',
                  {'data': data, 'name': cat_name.name, 'discription': cat_name.discription,
                   'popular': popular_product})


def product(request, id_prod):
    products = Product.objects.all()
    data = products.get(id=id_prod)
    popular_product = random.sample(list(products), 6)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/product.html', {'product': data, 'popular': popular_product,
                                                 'cart_product_form': cart_product_form})


def search_results(request):
    query = request.GET.get('q')
    object_list = Product.objects.filter(name__icontains=query)
    products = Product.objects.all()
    popular_product = random.sample(list(products), 6)
    return render(request, 'main/search_results.html', {'object_list': object_list, 'popular': popular_product})


