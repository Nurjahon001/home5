# Generated by Django 5.0.3 on 2024-03-21 21:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('ordered_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'orders_table',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'products_table',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='order.OrderItem', to='order.product'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_to', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product')),
            ],
            options={
                'db_table': 'discounts_table',
            },
        ),
    ]
