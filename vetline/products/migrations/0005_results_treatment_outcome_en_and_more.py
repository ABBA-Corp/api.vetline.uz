# Generated by Django 4.0.8 on 2023-03-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_results_subtitle_en_alter_results_subtitle_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='treatment_outcome_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='treatment_outcome_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='results',
            name='treatment_outcome_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
