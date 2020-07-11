from django.db import models
from django.utils import timezone

# User imports
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Search complex queries imports
from django.db.models import Q

class TherapistQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte = now)

	def search(self,query):
		lookup = (Q(name__icontains=query.split("_")[0]) | Q(condition__icontains=query.split("_")[1]) | Q(ethnicity__icontains=query.split("_")[2])
			| Q(city__icontains=query.split("_")[3]) | Q(state__icontains=query.split("_")[4]) | Q(zipcode__icontains=query.split("_")[5]) )
		# return self.filter(name__iexact=query)
		# return self.filter(name__icontains=query)
		return self.filter(lookup)

class TherapistManager(models.Manager):

	def get_queryset(self):
		return TherapistQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()

	def search(self, query= None):
		if query is None:
			return self.get_queryset().none()
		else:
			# return self.get_queryset().published().search(query)
			return self.get_queryset().search(query)

# Create your models here.
class Therapist(models.Model):

	"""
	Therapist class defines a therapist object based on geographical and demographical information
	
	Note that all geographical fields a name are required to define a therapist
	
	ToDo:
	
	- Define what columns will be included in 'condition' - I.e specs, issues, mental_health?
	- As a pacient may be described by multiple conditions I turned that field into a TextField to loosen length restrictions
	- Define whether we want to turn 'modality' into 3 boolean fields - I.e. Individual, Group, Couple
	- What is resource type?
	- Therapist 'age' is not available. Remove it?
	- Online could be used to define whether therapy can be done remotely 

	"""
	# Django user and timestamp data
	user 			= 	models.ForeignKey(User, default=1, null = True, on_delete = models.SET_NULL)
	# Therapist posting date
	publish_date = models.DateTimeField(auto_now = False,auto_now_add = False, null=True, blank = True)
	# Creation time (automatic)
	timestamp = models.DateTimeField(auto_now_add = True)
	# Updated time (automatic)
	updated = models.DateTimeField(auto_now = True)

	# Therapists Manager
	objects = TherapistManager()

	# Profile pic
	image			= 	models.ImageField(upload_to='image/', blank = True, null = True)

	# Therapist geographical info
	city 			=	models.CharField(max_length=255, null = False, blank = False)
	state 			=	models.CharField(max_length=255, null = False, blank = False)
	zipcode 		= 	models.PositiveIntegerField(null = False, blank = False)
	phone			= 	models.CharField(max_length=255, null = True, blank = True)

	# Therapist demographical info
	name 			= 	models.CharField(max_length=255, null = False, blank = False)

	# Therapy information / Patient requirements
	condition 		= 	models.TextField(null = True, blank = True) 
	ethnicity 		= 	models.CharField(max_length=255, null = True, blank = True)
	language 		= 	models.CharField(max_length=255, null = True, blank = True)
	sexuality 		= 	models.CharField(max_length=255, null = True, blank = True)
	therapy_type 	= 	models.CharField(max_length=255, null = True, blank = True)
	modality 		=	models.CharField(max_length=255, null = True, blank = True)

	class Meta:
		# Ordering based on 'variable' including "-" -> reverse ordering
		# I.e: '-publish_date' -> newest object first
		ordering = ['-publish_date', '-updated', '-timestamp']

	def get_absolute_url(self):
		return f"/therapist/{self.id}"

	def get_update_url(self):
		return f"{self.get_absolute_url()}/update"
		# return f"/therapist/{self.id}/update"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"
		# return f"/therapist/{self.id}/delete"

	# Other available fields
	# resource_type 	= 	models.CharField(max_length=255, null = True, blank = True)
	# age_focus			= 	models.CharField(max_length=255, null = True, blank = True)
	# com_focus			= 	models.CharField(max_length=255, null = True, blank = True)
	# faith			= 	models.CharField(max_length=255, null = True, blank = True)
	# age 			= 	models.PositiveSmallIntegerField(null = True, blank = True)

	# session_cost		= 	models.PositiveSmallIntegerField(null = True, blank = True)
	# pay_options		= 	models.CharField(max_length=255, null = True, blank = True)
	# insurance			= 	models.TextField(null = True, blank = True)
	# online			= 	models.BooleanField(null = True, blank = True)

	# Slug Field
	# slug 		= models.SlugField(unique = True)
	

	
	