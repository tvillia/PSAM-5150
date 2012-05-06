from django.contrib import admin
from census.models import CensusModel
#from census.models import AddressModel
#from census.models import ResidenceModel
#from census.models import RespondentModel

class CensusAdmin(admin.ModelAdmin)
	list_display = ('name', 'sex', 'dob', 'latinohispanic', 'race')
	#, 'address', 'city', 'state', 'zip', 'owned', 'number_of_residents', 'number_of_guests', 'name', 'address', 'city', 'state', 'zip', 'phone'

admin.site.register(CensusModel, CensusAdmin)
#AddressModel, ResidenceModel, RespondentModel, 