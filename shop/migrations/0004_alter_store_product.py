# Generated by Django 4.2.2 on 2023-06-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_store_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='product',
            field=models.ManyToManyField(blank=True, to='shop.product'),
        ),
    ]
