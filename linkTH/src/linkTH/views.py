from django.shortcuts import render
from django.template.loader import get_template

# Import Therapist
from therapist.models import Therapist

def home_page(request):
	
	my_title = "Welcome to linkTH!"
	context = {"title": my_title}
	return render(request, "home.html", context)



# def home_page(request):
# 	my_title = "Welcome to findTH!"
# 	qs = BlogPost.objects.all()[:5]
# 	context = {"title": my_title, 'blog_list': qs}
# 	return render(request, "home.html", context)

# def about_page(request):
# 	return render(request, "about.html", {"title": "About"})

# Import ContactForm
from .forms import ContactForm

def contact_page(request):
	# from django.http import HttpResponse
	# return HttpResponse("<h1>Contact us</h1>")

	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		# Re-init form
		form = ContactForm()

	context = {
		"title": "Contact Us", 
		"form": form
		}
	
	return render(request, "form.html", context)
