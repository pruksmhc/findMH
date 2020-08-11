from django.shortcuts import render, get_object_or_404, redirect

# Show only some entries
# from django.utils import timezone

# Request a user to be logged-in to perfom an action
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Models and Forms Imports
from .models import Therapist

# Import forms
# from .forms import TherapistForm
from .forms import TherapistModelForm

# CRUD (Create Retrieve Update Delete)

# GET -> Retrieve / List 
# POST -> Create / Update / Delete

######################################################

def therapist_detail_view(request, th_id):
	obj = get_object_or_404(Therapist, id=th_id)
	template_name = 'therapist/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)

def therapist_list_view(request):
	# qs = Therapist.objects.all()
	qs = Therapist.objects.all().published()

	# To view all post Created by 'user' + Published ones
	if request.user.is_authenticated:
		my_qs = Therapist.objects.filter(user = request.user)
		qs = (qs | my_qs).distinct()

	template_name = 'therapist/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)

# @login_required
@staff_member_required
def therapist_create_view(request):
	# Approach I) Using ModelForms
	form = TherapistModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit = False)
		# Associate form to one specific user...
		# Only include this once we have added 'user' to our model!
		obj.user = request.user
		obj.save()
		form = TherapistModelForm()

	template_name = 'therapist/form.html'
	context = {'form': form}
	return render(request, template_name, context)

@staff_member_required
def therapist_update_view(request, th_id):
	obj = get_object_or_404(Therapist, id=th_id)
	form = TherapistModelForm(request.POST or None, request.FILES or None, instance = obj)
	if form.is_valid():
		# form.save()
		obj = form.save(commit = False)
		# Associate form to one specific user...
		# Only include this once we have added 'user' to our model!
		obj.save()
	template_name = 'therapist/form.html'
	context = {'form': form, "title": f"Update {obj.name}"}
	return render(request, template_name, context)

@staff_member_required
def therapist_delete_view(request, th_id):
	obj = get_object_or_404(Therapist, id=th_id)
	template_name = 'therapist/delete.html'
	if request.method == 'POST':
		obj.delete()
		return redirect("/therapist")
	context = {"object": obj}
	return render(request, template_name, context)



####################################################
# Deprecated Views

# def therapist_detail_page(request, th_id = 1):

# 	obj = get_object_or_404(Therapist,id=th_id)
# 	template_name = 'therapist_detail.html'
# 	context = {"object": obj}
# 	return render(request, template_name, context)


