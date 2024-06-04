# Generated by Django 4.1.4 on 2023-01-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='slug'),
        ),
    ]
