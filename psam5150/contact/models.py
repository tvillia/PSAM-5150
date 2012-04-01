from django.db import models

class Contact(models.Model):

	name = models.CharField(max_length=100)
	address = models.charField(max_length_length=200)
	# Create your models here.
