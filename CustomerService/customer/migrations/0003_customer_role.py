# Generated by Django 3.1.12 on 2025-02-27 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20250226_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('seller', 'Seller'), ('buyer', 'Buyer'), ('guest', 'Guest')], default='buyer', max_length=10),
        ),
    ]
