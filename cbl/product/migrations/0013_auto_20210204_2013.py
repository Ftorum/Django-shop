# Generated by Django 3.0.8 on 2021-02-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20201115_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='keywords',
            field=models.CharField(max_length=255, verbose_name='Ключевое слово'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='keywords',
            field=models.CharField(max_length=255, verbose_name='Ключевое слово'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(default=0, verbose_name='Вес'),
        ),
    ]