# Generated by Django 4.0.6 on 2022-07-14 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productportfolio',
            old_name='discriptions',
            new_name='descriptions',
        ),
    ]
