from django import forms

from contact.models import ContactModel

#ContactForm
class ContactForm(forms.Form):
	name = forms.CharField()
	address = forms.CharField()
	city = forms.CharField()
	state = forms.CharField()
	zip = forms.IntergerField()
	phone = forms.IntergerField()
	email = forms.EmailField()
	subject = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)