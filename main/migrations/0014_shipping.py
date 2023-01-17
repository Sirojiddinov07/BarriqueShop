# Generated by Django 4.1.4 on 2022-12-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_cart_remove_order_customer_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('note', models.TextField()),
            ],
        ),
    ]