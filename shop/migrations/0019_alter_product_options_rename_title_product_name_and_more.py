# Generated by Django 4.0.6 on 2022-07-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_remove_review_star_review_grade_delete_star'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width',
        ),
        migrations.AddField(
            model_name='product',
            name='poster',
            field=models.ImageField(blank=True, upload_to='products/poster'),
        ),
    ]
