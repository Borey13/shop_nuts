# Generated by Django 4.2.3 on 2023-10-12 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_category_link_foto_remove_product_link_foto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]