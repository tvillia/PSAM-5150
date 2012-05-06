from django import forms

from census.models import CensusModel
'''
from census.models import AddressModel
from census.models import ResidenceModel
from census.models import RespondentModel
'''

class CensusForm(forms.Form):
	name = forms.CharField()
	sex = forms.CharField()
	dob = forms.IntegerField()
	latinohispanic = forms.CharField()
	race = forms.CharField()
'''
class AddressForm(forms.Form)
	address = forms.CharField(max_length=200)
	city = forms.Charfield(max_length=100)
	state = forms.CharField(max_length=2)
	zip = forms.IntegerField(max_length=5)

class ResidenceForm(forms.Form)
	owned = forms.BooleanField(default=False)
	number_of_residents = forms.IntegerField(max_length=2)
	number_of_guests = forms.IntegerField(max_length=2)

class RespondentForm(forms.Form)
	name = forms.CharField(max_length=100)
	address = forms.CharField(max_length=200)
	city = forms.Charfield(max_length=100)
	state = forms.CharField(max_length=2)
	zip = forms.IntegerField(max_length=5)
	phone = forms.IntegerField(max_length=10)
'''