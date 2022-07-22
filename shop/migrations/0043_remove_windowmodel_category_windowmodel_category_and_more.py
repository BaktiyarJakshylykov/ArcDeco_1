# Generated by Django 4.0.6 on 2022-07-22 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_window_model_remove_windowmodel_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='windowmodel',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='window', to='shop.window'),
        ),
        migrations.DeleteModel(
            name='Window_Model',
        ),
    ]