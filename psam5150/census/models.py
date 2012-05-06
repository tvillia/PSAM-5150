from django.db import models

#CensusModel...
class CensusModel(models.Model):
	
	name = models.CharField(max_length=100)
	sex = models.CharField(max_length=1)
	dob = models.IntegerField(max_length=8)
	latinohispanic = models.CharField(max_length=1)
	race = models.CharField(max_length=100)

'''
class AddressModel(model.Model)
	address = models.CharField(max_length=200)
	city = models.Charfield(max_length=100)
	state = models.CharField(max_length=2)
	zip = models.IntegerField(max_length=5)

class ResidenceModel(model.Model)
	owned = models.BooleanField(default=False)
	number_of_residents = models.IntegerField(max_length=2)
	number_of_guests = models.IntegerField(max_length=2)

class RespondentModel(model.Model)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.Charfield(max_length=100)
	state = models.CharField(max_length=2)
	zip = models.IntegerField(max_length=5)
	phone = models.IntegerField(max_length=10)
'''

