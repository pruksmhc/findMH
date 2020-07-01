from django.db import models

# Associate Blog Post to a User with Foreign Keys
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model): # blogpost_set -> would give me queryset ( See 'cfe' Associate BlogPost to a user with Foreign Key for more info...
	# id = models.IntegerField() # pk

	user = models.ForeignKey(User, default = 1, null=True, on_delete= models.SET_NULL)
	# user = models.ForeignKey(User, default = 1, null=True, on_delete= models.CASCADE)

	title 	= models.CharField(max_length = 120)
	slug	= models.SlugField(unique = True)
	content = models.TextField(null = True, blank = True)

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
