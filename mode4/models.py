from django.db import models
from django.forms import ModelForm

# Create your models here.
class Input(models.Model):
	x = models.FloatField(
		verbose_name=' ε_x', default=0)
	y = models.FloatField(
		verbose_name=' ε_y', default=0)
	xy = models.FloatField(
		verbose_name=' γ_xy', default=0)
	setta = models.FloatField(
		verbose_name=' ϑ', default=0)
	unit = models.IntegerField(
		verbose_name='unit', default=-6, help_text='Please write the power of unit. ex) 2*10^(-6) => -6')


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['x', 'y', 'xy', 'setta', 'unit']
    
