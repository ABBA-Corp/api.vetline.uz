# Generated by Django 4.0.8 on 2023-02-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_top',
            field=models.BooleanField(default=False, verbose_name='На топе?'),
        ),
    ]
