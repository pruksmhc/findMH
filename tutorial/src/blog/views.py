# To request user to be logged in to perfom 'x' action
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import BlogPost

# Import forms
from .forms import BlogPostForm
from .forms import BlogPostModelForm


def blog_post_detail_page_id(request, post_id):
	obj = get_object_or_404(BlogPost,id=post_id)
	# try:
	# 	obj = BlogPost.objects.get(id= post_id)
	# except BlogPost.DoesNotExist:
	# 	raise Http404
	# except ValueError:
	# 	raise Http404
	template_name = 'blog_post_detail.html'
	context = {"object": obj}
	return render(request, template_name, context)


# CRUD (Create Retrieve Update Delete)

# GET -> Retrieve / List - 1 object
# POST -> Create / Update / Delete

# filter -> [] objects


def blog_post_list_view(request):
	# list our objects 
	# could be search
	qs = BlogPost.objects.all() # queryset -> list of python objecsts
	# more advanced search
	# qs = BlogPost.objects.filter(title__icontains='hello')
	template_name = 'blog/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)

# @login_required(login_url='/login')
# @login_required() # If you use this - Please set LOGIN options in settings.py
@staff_member_required
def blog_post_create_view(request):
	# create objects
	# ? use a form
	# request.user -> return something
	# Approach I) Using ModelForms
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit = False)
		# Only include once we have added user to our model!!! 
		obj.user = request.user
		obj.save()
		form = BlogPostModelForm()

		# Extra if we wanna make changes to form input
		# obj = form.save(commit= False)
		# obj.title = form.cleaned_data.get("title") + "0"
		# obj.save()

	# # Approach II) Using Forms
	# form = BlogPostForm(request.POST or None)
	# if form.is_valid():
	# 	# print(form.cleaned_data)
	# 	# title = form.cleaned_data['title']
	# 	# obj = BlogPost.objects.create(title = title)
	# 	obj = BlogPost.objects.create(**form.cleaned_data)
	# 	form = BlogPostForm()


	# Notice I'll be using the main one (not the one in blog template)
	template_name = 'form.html'
	# template_name = 'blog/create.html'
	context = {'form': form}
	return render(request, template_name, context)

def blog_post_detail_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
	# 1 object -> detail view
	obj = get_object_or_404(BlogPost,slug=slug)
	form = BlogPostModelForm(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()

	# template_name = 'blog/update.html'
	template_name = 'form.html'
	context = {'form': form, "title": f"Update {obj.title}"}
	return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
	# 1 object -> detail view
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name = 'blog/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect('/blog')

	context = {"object": obj}
	return render(request, template_name, context)


# Deleted material

# def blog_post_detail_page(request, slug):
# 	# queryset = BlogPost.objects.filter(slug=slug)
# 	# if queryset.count() == 0:
# 	# 	raise Http404
# 	# obj = queryset.first()
# 	obj = get_object_or_404(BlogPost,slug=slug)
# 	template_name = 'blog_post_detail.html'
# 	context = {"object": obj}
# 	return render(request, template_name, context)