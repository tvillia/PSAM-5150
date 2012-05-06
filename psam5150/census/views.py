# Create your views here...
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from census.forms import PersonForm
from census.forms import AddressForm
from census.forms import ResidenceForm
from census.forms import RespondentForm

from census.models import PersonModel 
from census.models import AddressModel
from census.models import ResidenceModel
from census.models import RespondentModel

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def received(request):
	return render_to_response('census/received.html', context_instance=RequestContext(request))

def dolai_census(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			dolai_census = PersonModel()
			dolai_census.name = form.cleaned_data['name']
			dolai_census.sex = form.cleaned_data['sex']
			dolai_census.dob = form.cleaned_data['dob']
			dolai_census.latinohispanic = form.cleaned_data['latinohispanic']
			dolai_census.race = form.cleaned_data['race']
			dolai_census.save()
			return redirect('received')

	else:
		form = PersonForm()

	return render_to_response('census/dolaicensus.html', {'form':form},
		context_instance=RequestContext(request))

