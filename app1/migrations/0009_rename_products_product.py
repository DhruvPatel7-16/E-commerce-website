# Generated by Django 4.2.10 on 2024-03-22 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0008_products"),
    ]

    operations = [
        migrations.RenameModel(old_name="products", new_name="product",),
    ]
