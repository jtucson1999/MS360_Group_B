from django.shortcuts import render
from mode1.models import InputForm 
from mode1.compute import compute
import os

# Create your views here.

def mode1(request):
	#os.chdir(os.path.dirname(__file__))
	result = [None, None, None]
	unit = None
	if request.method == 'POST':
		form = InputForm(request.POST)
		if form.is_valid():
			form2 = form.save(commit=False)
			result = compute(form2.x, form2.y, form2.xy, form2.setta)
			unit = form2.unit
	else: 
		form = InputForm()
		
	return render(request, 'mode1.html', {
		'form' : form,
		'sigmax' : result[0],
		'sigmay' : result[1],
		'tauxy' : result[2],
		'unit' : unit
		})



