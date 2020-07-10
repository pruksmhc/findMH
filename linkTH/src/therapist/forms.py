from django import forms

from .models import Therapist

# Preferable method (forms.ModelForm)

class TherapistModelForm(forms.ModelForm):

	class Meta:
		model = Therapist
		fields = ['city', 'state',  'zipcode', 'phone', 'name', 'image',
		'condition', 'ethnicity', 'language', 'sexuality', 
		'therapy_type', 'modality', 'publish_date']


	def clean_name(self, *args, **kwargs):

		'''
		Method for attribute validation -> 'name'
		'''
		name = self.cleaned_data.get('name')
		
		# Filtering name
		# qs = Therapist.objects.filter(name=name)
		# Filter fuzzy string
		# qs = Therapist.objects.filter(name__icontains=name)
		# Filter exact same string
		qs = Therapist.objects.filter(name__iexact=name)

		instance = self.instance
		if instance is not None:
			qs = qs.exclude(pk=instance.pk) # pk (primary key) == id = instance.id

		if qs.exists():
		 	raise forms.ValidationError("This name has already been used. Please try again")

		return name

# Rudimentary method (forms.Form)
# class BlogPostForm(forms.Form):

# 	city = forms.CharField()
# 	state = forms.CharField()
# 	zipcode = forms.PositiveIntegerField()
# 	name = forms.CharField()
