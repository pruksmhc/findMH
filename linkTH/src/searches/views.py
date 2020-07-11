from django.shortcuts import render

# Import searches model
from .models import SearchQuery
# Import therapist model
from therapist.models import Therapist

# Create your views here.
def search_view(request):
	city = request.GET.get('city', None)
	zipc = request.GET.get("zip", None)
	condition = request.GET.get("condition", None)
	modality = request.GET.get("modality", None)
	ethnicity = request.GET.get("ethnicity", None)
	lang = request.GET.get("language", None)
	sexuality = request.GET.get("sexuality", None)
	query = "_".join([city, zipc, condition, modality, ethnicity, lang, sexuality])
	user = None
	if request.user.is_authenticated:
		user = request.user

	context = {"query": query}

	if query is not None:
		SearchQuery.objects.create(user = user, query = query)
		th_list = Therapist.objects.search(query=query)
		context['th_list'] = th_list
	
	return render(request, 'searches/view.html', context)

# Create Advance Search View