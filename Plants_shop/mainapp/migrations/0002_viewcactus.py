# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-06 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
                ('complexity_of_cultivation', models.CharField(max_length=16, verbose_name='Сложность выращивания')),
                ('price', models.FloatField(blank=True, verbose_name='Цена')),
                ('area', models.CharField(max_length=32, unique=True, verbose_name='Меcто прозизрастания')),
                ('diametr', models.CharField(max_length=32, unique=True, verbose_name='Диаметр сеянцев(мм)')),
                ('genus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.CactusGenus', verbose_name='Род')),
            ],
        ),
    ]