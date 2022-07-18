# Generated by Django 4.0.6 on 2022-07-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_product_options_rename_title_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='наличие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='фото продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='poster',
            field=models.ImageField(blank=True, upload_to='products/poster', verbose_name='размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uploded',
            field=models.DateTimeField(auto_now=True, verbose_name='дата обновление'),
        ),
    ]