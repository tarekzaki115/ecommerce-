# Generated by Django 5.0.4 on 2024-08-28 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0007_remove_cart_address_remove_cart_created_at_and_more"),
        ("user", "0002_address"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Address",
        ),
    ]