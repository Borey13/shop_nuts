# Generated by Django 4.2.3 on 2023-10-21 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_productcalories_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcalories',
            name='product',
        ),
    ]