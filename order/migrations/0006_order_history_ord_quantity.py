# Generated by Django 3.2.6 on 2021-08-29 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210829_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_history',
            name='ord_quantity',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
