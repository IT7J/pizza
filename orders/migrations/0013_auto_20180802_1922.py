# Generated by Django 2.0.7 on 2018-08-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20180802_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cartitems',
        ),
        migrations.AddField(
            model_name='cart',
            name='cartitems_pasta',
            field=models.ManyToManyField(blank=True, related_name='cart', to='orders.Pasta'),
        ),
    ]