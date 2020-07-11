from django.conf import settings
from django.db import models

# Create your models here.
class SearchQuery(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, blank = True, null = True, on_delete=models.SET_NULL)
	query 		= models.CharField(max_length=220)
	"""
	#zip_query 		= models.CharField(max_length=220)
	location_query 	= models.CharField(max_length=220)
	condition_query 	= models.CharField(max_length=220)
	modality_query 	= models.CharField(max_length=220)
	ethnicity_query 	= models.CharField(max_length=220)
	language_query 	= models.CharField(max_length=220)
	sexuality_query 	= models.CharField(max_length=220)
	"""
	timestamp 	= models.DateTimeField(auto_now_add=True)