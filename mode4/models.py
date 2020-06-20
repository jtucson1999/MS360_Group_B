from django.db import models
from django.forms import ModelForm

# Create your models here.
class Input(models.Model):
	x = models.FloatField(
		verbose_name=' ε_x', default=0, help_text='Normal strain along x direction.')
	y = models.FloatField(
		verbose_name=' ε_y', default=0, help_text='Normal strain along y direction.')
	xy = models.FloatField(
		verbose_name=' γ_xy', default=0, help_text='Shear strain.')
	setta = models.FloatField(
		verbose_name=' ϑ', default=0, help_text='Rotation angle.')
	unit = models.IntegerField(
		verbose_name='unit', default=-6, help_text='Please write the power of unit. ex) 2*10^(-6) => -6')


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['x', 'y', 'xy', 'setta', 'unit']
    
