# Generated by Django 2.0.7 on 2018-08-02 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180802_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Cartitem',
            new_name='cartitems',
        ),
    ]