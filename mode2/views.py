from django.shortcuts import render
from mode2.models import InputForm 
from mode2.compute import compute
import os

# Create your views here.

def mode2(request):
	os.chdir(os.path.dirname(__file__))
	result = [None, None, None, None]
	unit = None
	if request.method == 'POST':
		form = InputForm(request.POST)
		if form.is_valid():
			form2 = form.save(commit=False)
			result = compute(form2.x, form2.y, form2.xy)
			unit = form2.unit
			
	else: 
		form = InputForm()
		
	
	return render(request, 'mode2.html', {
		'form' : form,
		'angle1' : result[0],
		'angle2' : result[1],
		'sigma1' : result[2],
		'sigma2' : result[3],
		'unit' : unit
		})
