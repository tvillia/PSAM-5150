# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from contact.forms import ContactForm

from contact.models import ContactModel 

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def received(request):
	return render_to_response('contact/received.html', context_instance=RequestContext(request))

def dolai_contact(request):
	if request.method == 'POST': #does this need to be capitalized? I wonder what will happen if I take that away. Remember to try that later
		form = ContactForm(request.POST)
		if form.is_valid():
			my_contacts = ContactModel()
			my_contacts.name = form.cleaned_data['name']
			my_contacts.address = form.cleaned_data['address']
			my_contacts.city = form.cleaned_data['city']
			my_contacts.state = form.cleaned_data['state']
			my_contacts.zip = form.cleaned_data['zip']
			my_contacts.phone = form.cleaned_data['phone']
			my_contacts.email = form.cleaned_data['email']
			my_contacts.subject = form.cleaned_data['subject']
			my_contacts.message = form.cleaned_data['message']
			my_contacts.save()
			return redirect('received')
	else:
		form = ContactForm()
	return render_to_response('contact/dolaicontact.html',{'form':form}, context_instance=RequestContext(request))