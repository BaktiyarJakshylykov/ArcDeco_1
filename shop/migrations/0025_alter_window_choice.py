# Generated by Django 4.0.6 on 2022-07-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_alter_window_options_remove_unitfmeasurement_p_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='window',
            name='choice',
            field=models.CharField(choices=[('PM', 'П.М'), ('ST', 'ШТ')], default='PM', max_length=2, verbose_name='25см оставить'),
        ),
    ]
