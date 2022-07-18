# Generated by Django 4.0.6 on 2022-07-18 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_remove_window_category_remove_window_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='window',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Каличество'),
        ),
        migrations.AddField(
            model_name='window',
            name='count_detail',
            field=models.IntegerField(default=0, verbose_name='Каличество для деталя'),
        ),
        migrations.AddField(
            model_name='window',
            name='measurement_detail',
            field=models.CharField(choices=[('PM', 'П.М'), ('ST', 'ШТ')], default='PM', max_length=2, verbose_name='единица измерения для деталя'),
        ),
        migrations.AddField(
            model_name='window',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='window',
            name='price_detail',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, verbose_name='цена для деталя'),
        ),
        migrations.AddField(
            model_name='window',
            name='product_detail',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='shop.product', verbose_name='продукция для деталя'),
        ),
    ]