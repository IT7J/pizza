# Generated by Django 2.0.7 on 2018-07-31 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180730_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subs',
            name='small',
            field=models.FloatField(blank=True),
        ),
    ]