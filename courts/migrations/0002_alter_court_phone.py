# Generated by Django 3.2.8 on 2021-10-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='phone',
            field=models.CharField(blank=True, help_text='Court phone number', max_length=20),
        ),
    ]