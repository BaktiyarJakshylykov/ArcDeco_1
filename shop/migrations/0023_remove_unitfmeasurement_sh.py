# Generated by Django 4.0.6 on 2022-07-15 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_unitfmeasurement_alter_product_category_window'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitfmeasurement',
            name='sh',
        ),
    ]
