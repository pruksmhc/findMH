from django.db import models

# Associate Blog Post to a User with Foreign Keys
from django.conf import settings

# Import for model manager
from django.utils import timezone

# Complex queries
from django.db.models import Q

User = settings.AUTH_USER_MODEL

# Create your models here.

class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		# BlogPost.objects.all()
		return self.filter(publish_date__lte = now)

	def search(self,query):
		lookup = (Q(title__icontains=query) | Q(content__icontains=query) )
		lookup = (Q(title__icontains=query) | Q(content__icontains=query) | Q(user__last_name__icontains=query) ) 
		# return self.filter(title__iexact=query)
		# return self.filter(title__icontains=query)
		return self.filter(lookup)

class BlogPostManager(models.Manager):

	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self.db)

	def published(self):
		return self.get_queryset().published()

	def search(self, query= None):
		if query is None:
			return self.get_queryset().none()
		else:
			# return self.get_queryset().published().search(query)
			return self.get_queryset().search(query)


class BlogPost(models.Model): # blogpost_set -> would give me queryset ( See 'cfe' Associate BlogPost to a user with Foreign Key for more info...
	# id = models.IntegerField() # pk

	user = models.ForeignKey(User, default = 1, null=True, on_delete= models.SET_NULL)
	# user = models.ForeignKey(User, default = 1, null=True, on_delete= models.CASCADE)
	# image = models.FileField(upload_to = 'images/', blank = True, null = True)
	image = models.ImageField(upload_to = 'images/', blank = True, null = True)
	title 	= models.CharField(max_length = 120)
	slug	= models.SlugField(unique = True)
	content = models.TextField(null = True, blank = True)
	publish_date = models.DateTimeField(auto_now = False,auto_now_add = False, null=True, blank = True)
	# Creation time (automatic)
	timestamp = models.DateTimeField(auto_now_add = True)
	# Updated time (automatic)
	updated = models.DateTimeField(auto_now = True)

	objects = BlogPostManager()

	class Meta:
		ordering = ['-publish_date', '-updated', '-timestamp']


	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	# def get_edit_url(self):
	# 	return f"/blog/{self.slug}/edit"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"

	# def get_delete_url(self):
	# 	return f"/blog/{self.slug}/delete"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"
