# Generated by Django 3.2.6 on 2021-08-29 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_history_ord_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='chekout_color',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='chekout_quantity',
        ),
    ]