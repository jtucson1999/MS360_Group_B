from django.db import models
from django.forms import ModelForm

# Create your models here.
class Input(models.Model):
	UNIT_OF_PASCAL_CHOICES = [
	('GPa','GPa'), 
	('MPa','MPa'), 
	('kPa','kPa'),
	('Pa','Pa'),
	]
	x = models.FloatField(
		verbose_name=' σ_x', default=0)
	y = models.FloatField(
		verbose_name=' σ_y', default=0)
	xy = models.FloatField(
		verbose_name=' τ_xy', default=0)
	unit = models.CharField(max_length=3,
		verbose_name='unit', choices= UNIT_OF_PASCAL_CHOICES, default='MPa')

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['x', 'y', 'xy', 'unit']
    
