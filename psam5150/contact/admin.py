from django.contrib import admin
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'city', 'state', 'zip', 'phone', 'subject', 'email')

admin.site.register(Contact, ContactAdmin)