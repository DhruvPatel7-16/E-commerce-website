# Generated by Django 4.2.10 on 2024-03-30 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0016_rename_vendor_vendors"),
    ]

    operations = [
        migrations.RenameModel(old_name="vendors", new_name="vendor",),
    ]