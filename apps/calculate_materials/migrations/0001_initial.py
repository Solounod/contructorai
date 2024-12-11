# Generated by Django 4.2 on 2024-12-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrompMainAi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promp_main', models.TextField(verbose_name='Prompt')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug_promp', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name='Fecha creacion')),
                ('update_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha modificacion')),
            ],
        ),
    ]