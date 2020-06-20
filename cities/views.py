from django.shortcuts import render
# cities/views.py
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        # TODO: Make some NLP pipeline to extract key words here.
        field_types = ["Ethnicity", "gender"]
        field_values = ["Asian", "female"]
        results = []
        """
        for i in range(len(field_types)):
            object_list = City.objects.get( Q.get(field_types[i] +"__iexact"= field_values[i]) 
            )
            results.extend(object_list)
        """
        return results
# Create your views here.
