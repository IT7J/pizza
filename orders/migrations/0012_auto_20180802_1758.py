# Generated by Django 2.0.7 on 2018-08-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cartitems',
            field=models.ManyToManyField(blank=True, related_name='cart', to='orders.Menu'),
        ),
    ]
