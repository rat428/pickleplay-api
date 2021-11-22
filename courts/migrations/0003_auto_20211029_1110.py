# Generated by Django 3.2.8 on 2021-10-29 11:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_alter_court_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='court',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), default=[], size=None),
        ),
    ]
