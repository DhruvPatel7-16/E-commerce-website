# Generated by Django 4.2.10 on 2024-04-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0017_rename_vendors_vendor"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="vendorid",
            field=models.CharField(default=" ", max_length=20),
        ),
    ]
