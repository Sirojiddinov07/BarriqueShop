# Generated by Django 4.1.4 on 2022-12-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cart_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
