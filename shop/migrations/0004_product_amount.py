# Generated by Django 4.0.6 on 2022-07-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_poster_product_poster1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
