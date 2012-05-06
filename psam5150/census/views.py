# Create your views here...
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from census.forms import CensusForm
#from census.forms import AddressForm
#from census.forms import ResidenceForm
#from census.forms import RespondentForm

from census.models import CensusModel 
#from census.models import AddressModel
#from census.models import ResidenceModel
#from census.models import RespondentModel

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def received(request):
	return render_to_response('census/received.html', context_instance=RequestContext(request))

def dolai_census(request):
	if request.method == 'POST':
		form = CensusForm(request.POST)
		if form.is_valid():
			my_census = CensusModel()
			my_census.name = form.cleaned_data['name']
			my_census.sex = form.cleaned_data['sex']
			my_census.dob = form.cleaned_data['dob']
			my_census.latinohispanic = form.cleaned_data['latinohispanic']
			my_census.race = form.cleaned_data['race']
			my_census.save()
			return redirect('received')

	else:
		form = CensusForm()
	return render_to_response('census/dolaicensus.html',{'form':form}, context_instance=RequestContext(request))

