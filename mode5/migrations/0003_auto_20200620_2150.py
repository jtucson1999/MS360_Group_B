# Generated by Django 3.0.7 on 2020-06-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mode5', '0002_auto_20200620_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='unit',
            field=models.IntegerField(default=-6, help_text='Please write the power of unit. ex) 2*10^(-6) => -6', verbose_name='unit'),
        ),
    ]
