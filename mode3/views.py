from django.shortcuts import render
from django.http import HttpResponse
from mode3.models import InputForm 
from mode3.compute import compute
import os

# Create your views here.

def mode3(request):
	os.chdir(os.path.dirname(__file__))
	result = [None, None, None]
	unit = None
	if request.method == 'POST':
		form = InputForm(request.POST)
		if form.is_valid():
			form2 = form.save(commit=False)
			result = compute(form2.x, form2.y, form2.xy)
			unit = form2.unit
			
	else: 
		form = InputForm()
		

	
	return render(request, 'mode3.html', {
		'form' : form,
		'angle1' : result[0],
		'angle2' : result[1],
		'max_tau' : result[2],
		'unit' : unit
		})
