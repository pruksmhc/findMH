from django.shortcuts import render

# Import searches model
from .models import SearchQuery
# Import therapist model
from therapist.models import Therapist

# Create your views here.
def search_view(request):
	query = request.GET.get('q', None)
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