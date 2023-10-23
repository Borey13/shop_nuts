from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'email', 'mobile',
                    'city', 'address', 'created', 'accept']
    list_filter = ['created', 'accept']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

