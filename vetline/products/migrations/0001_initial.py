# Generated by Django 4.0.8 on 2023-02-03 10:28

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields
import vetline.products.instances


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name_uz', models.CharField(max_length=200)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_uz', models.CharField(max_length=200)),
                ('subtitle_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to=vetline.products.instances.get_shots_path, verbose_name='Изображение')),
                ('description_uz', models.TextField(verbose_name='Описание uz')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание en')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание ru')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Заголовок uz')),
                ('title_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок en')),
                ('title_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок ru')),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to=vetline.products.instances.get_results_path, verbose_name='Изображение')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='Категория продукта'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='product',
            order_with_respect_to='category',
        ),
    ]
