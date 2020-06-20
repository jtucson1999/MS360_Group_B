from django.db import models
from django.forms import ModelForm, MultipleChoiceField

# Create your models here.
class Input(models.Model):
	UNIT_OF_PASCAL_CHOICES = [
	('GPa','GPa'), 
	('MPa','MPa'), 
	('kPa','kPa'),
	('Pa','Pa'),
	]
	x = models.FloatField(
		verbose_name=' σ_x', default=0, help_text='Normal stress along x direction.')
	y = models.FloatField(
		verbose_name=' σ_y', default=0, help_text='Normal stress along y direction.')
	xy = models.FloatField(
		verbose_name=' τ_xy', default=0, help_text='Shear stress.')
	setta = models.FloatField(
		verbose_name=' ϑ ', default=0, help_text='Rotation angle.')
	unit = models.CharField(max_length=3,
		verbose_name='unit', choices= UNIT_OF_PASCAL_CHOICES, default='MPa', help_text='Unit of the stress.')


class InputForm(ModelForm):
	class Meta:
		model = Input
		fields = ['x', 'y', 'xy', 'setta', 'unit']

    
