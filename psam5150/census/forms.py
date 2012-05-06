from django import forms

from census.models import PersonModel
from census.models import AddressModel
from census.models import ResidenceModel
from census.models import RespondentModel

class PersonForm(forms.Form)
	name = forms.CharField(max_length=100)
	sex = forms.CharField(max_length=1)
	dob = forms.DateField()
	latinohispanic = forms.BooleanField(required=False)
	race = forms.CharField(max_length=100)

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