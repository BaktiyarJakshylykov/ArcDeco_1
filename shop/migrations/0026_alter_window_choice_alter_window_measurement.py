# Generated by Django 4.0.6 on 2022-07-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_alter_window_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='window',
            name='choice',
            field=models.CharField(choices=[('tr', 'Да'), ('fa', 'Нет')], default='PM', max_length=2, verbose_name='25см оставить'),
        ),
        migrations.AlterField(
            model_name='window',
            name='measurement',
            field=models.CharField(choices=[('PM', 'П.М'), ('ST', 'ШТ')], max_length=2, verbose_name='единица измерения'),
        ),
    ]
