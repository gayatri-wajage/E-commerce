# Generated by Django 5.1.3 on 2024-11-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cart_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
