# Generated by Django 2.2.14 on 2021-03-19 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaass', '0006_remove_pizza_rest_orders_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='all',
            options={'ordering': ['customers_info']},
        ),
    ]