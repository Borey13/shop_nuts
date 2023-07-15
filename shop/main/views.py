from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')


def category(request):
    return render(request, 'main/category.html')


def product(request):
    return render(request, 'main/product.html')
