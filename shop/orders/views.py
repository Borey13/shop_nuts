import random
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart

from main.models import Product


def order_create(request):
    products = Product.objects.all()
    popular_product = random.sample(list(products), 6)
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         total_price_product=item['price'] * item['quantity'] / 100,
                                         )
            cart.clear()

            return render(request, 'orders/created.html',
                          {'order': order, 'popular': popular_product})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, 'popular': popular_product})


def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    products = Product.objects.all()
    popular_product = random.sample(list(products), 6)
    return render(request, 'orders/my_orders.html', {'orders': orders, 'popular': popular_product})


def my_orders_items(request, id):
    products = Product.objects.all()
    popular_product = random.sample(list(products), 6)
    order = Order.objects.get(pk=id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'orders/my_orders_items.html', {'order_items': order_items,
                                                           'order': order,
                                                           'popular': popular_product
                                                           })
