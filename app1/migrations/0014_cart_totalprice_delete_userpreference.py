# Generated by Django 4.2.10 on 2024-03-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0013_userpreference"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="totalprice",
            field=models.CharField(default=" ", max_length=5),
        ),
        migrations.DeleteModel(name="UserPreference",),
    ]