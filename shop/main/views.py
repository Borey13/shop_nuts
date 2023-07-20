from django.shortcuts import render
from .models import Category, Product


def main(request):
    data = Category.objects.all()
    return render(request, 'main/main.html', {'categories': data})


def about(response):
    return render(response, 'main/about.html')


def category(response, id_cat):
    data = Product.objects.filter(category_id=id_cat)
    cat_name = Category.objects.get(category_id=id_cat)
    return render(response, 'main/category.html', {'data': data, 'name': cat_name.name})


def product(response, id_prod):
    data = Product.objects.get(id=id_prod)
    return render(response, 'main/product.html', {'product': data})
