from django.contrib import admin
from contact.models import ContactModel

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'city', 'state', 'zip', 'phone', 'subject', 'email')

admin.site.register(ContactModel, ContactAdmin)