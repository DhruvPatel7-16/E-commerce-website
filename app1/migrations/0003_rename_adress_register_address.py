# Generated by Django 4.2.10 on 2024-03-07 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_register"),
    ]

    operations = [
        migrations.RenameField(
            model_name="register", old_name="Adress", new_name="Address",
        ),
    ]