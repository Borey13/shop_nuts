from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'first_name', 'email', 'mobile',  'city', 'address']
