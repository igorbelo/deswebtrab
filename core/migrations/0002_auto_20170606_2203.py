# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 22:03
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pills',
            field=models.IntegerField(verbose_name='Quantidade (em p\xedlulas)'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='quantity_unit',
            field=models.CharField(blank=True, choices=[('mg', 'mg'), ('g', 'g'), ('kg', 'kg'), ('ml', 'ml'), ('l', 'l'), ('cx', 'cx')], max_length=2, null=True, verbose_name='Unidade'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='remedio',
            field=models.CharField(max_length=150, verbose_name='Rem\xe9dio'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='crm',
            field=models.CharField(max_length=10, verbose_name='CRM do M\xe9dico'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='doctor',
            field=models.CharField(max_length=150, verbose_name='Nome do M\xe9dico'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pills',
            field=models.IntegerField(verbose_name='Quantidade (em p\xedlulas)'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='prescription',
            field=models.FileField(upload_to=core.models.prescription_file_upload, verbose_name='Receita'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='quantity_unit',
            field=models.CharField(blank=True, choices=[('mg', 'mg'), ('g', 'g'), ('kg', 'kg'), ('ml', 'ml'), ('l', 'l'), ('cx', 'cx')], max_length=2, null=True, verbose_name='Unidade'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='remedio',
            field=models.CharField(max_length=150, verbose_name='Rem\xe9dio'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(verbose_name='Endere\xe7o'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.TextField(verbose_name='Descri\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='razao_social',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Raz\xe3o Social'),
        ),
    ]
