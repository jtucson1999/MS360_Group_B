from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def mode1(request):
	return render(request, 'mode1.html')

def mode2(request):
	return render(request, 'mode2.html')

def mode3(request):
	return render(request, 'mode3.html')

def mode4(request):
	return render(request, 'mode4.html')

def mode5(request):
	return render(request, 'mode5.html')

def mode6(request):
	return render(request, 'mode6.html')

