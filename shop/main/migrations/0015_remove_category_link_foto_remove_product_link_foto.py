# Generated by Django 4.2.3 on 2023-10-10 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='link_foto',
        ),
        migrations.RemoveField(
            model_name='product',
            name='link_foto',
        ),
    ]
