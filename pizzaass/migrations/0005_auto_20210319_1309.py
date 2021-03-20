# Generated by Django 2.2.14 on 2021-03-19 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaass', '0004_auto_20210319_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='orders',
        ),
        migrations.CreateModel(
            name='All',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizzaass.Customers')),
                ('pizza_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizzaass.Pizza_Rest')),
            ],
        ),
    ]