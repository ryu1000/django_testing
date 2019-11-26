import subprocess
import json
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm

# Create your views here.
def create_view(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			#print(**form.cleaned_data)
			form = MyForm()
	else:
		form = MyForm()
	
	data = { 'form' : form }
	return render(request, "create.html", data)

def run_view(request):
	if request.method == 'POST':
		out = subprocess.run(['bash', 'products/scripts/test.sh'], stdout=subprocess.PIPE)
		#subprocess.run(['pwd'])
		print(out.stdout)
		return HttpResponse(json.dumps({'name': str(out.stdout)}))
	else:
		return render(request, "run.html", {})