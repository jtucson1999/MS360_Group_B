# Generated by Django 3.0.7 on 2020-06-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mode3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='unit',
            field=models.CharField(choices=[('GPa', 'GPa'), ('MPa', 'MPa'), ('kPa', 'kPa'), ('Pa', 'Pa')], default='MPa', max_length=3, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='input',
            name='x',
            field=models.FloatField(default=0, verbose_name=' σ_x'),
        ),
        migrations.AlterField(
            model_name='input',
            name='xy',
            field=models.FloatField(default=0, verbose_name=' τ_xy'),
        ),
        migrations.AlterField(
            model_name='input',
            name='y',
            field=models.FloatField(default=0, verbose_name=' σ_y'),
        ),
    ]
