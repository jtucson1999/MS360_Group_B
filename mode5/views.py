from django.shortcuts import render
from django.http import HttpResponse
from mode5.models import InputForm 
from mode5.compute import compute
import os

# Create your views here.

def mode5(request):
	os.chdir(os.path.dirname(__file__))
	result = [None, [None, None, None, None]]
	unit = None
	if request.method == 'POST':
		form = InputForm(request.POST)
		if form.is_valid():
			form2 = form.save(commit=False)
			result = compute(form2.x, form2.y, form2.xy)
			unit = form2.unit	
	else: 
		form = InputForm()
		

	
	return render(request, 'mode5.html', {
		'form' : form,
		'result_image': result[0],
		'angle1' : result[1][0],
		'angle2' : result[1][1],
		'epsilon1' : result[1][2],
		'epsilon2' : result[1][3],
		'unit' : unit
		})
