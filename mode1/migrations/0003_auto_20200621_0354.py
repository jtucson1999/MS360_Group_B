# Generated by Django 3.0.7 on 2020-06-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mode1', '0002_auto_20200620_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='setta',
            field=models.FloatField(default=0, help_text='Rotation angle.', verbose_name=' ϑ '),
        ),
        migrations.AlterField(
            model_name='input',
            name='unit',
            field=models.CharField(choices=[('GPa', 'GPa'), ('MPa', 'MPa'), ('kPa', 'kPa'), ('Pa', 'Pa')], default='MPa', help_text='Unit of the stress.', max_length=3, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='input',
            name='x',
            field=models.FloatField(default=0, help_text='Normal stress along x direction.', verbose_name=' σ_x'),
        ),
        migrations.AlterField(
            model_name='input',
            name='xy',
            field=models.FloatField(default=0, help_text='Shear stress.', verbose_name=' τ_xy'),
        ),
        migrations.AlterField(
            model_name='input',
            name='y',
            field=models.FloatField(default=0, help_text='Normal stress along y direction.', verbose_name=' σ_y'),
        ),
    ]
