from django.contrib import admin

from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ("zipcode", "ethnicity", "age",  "language", "resource_type", "therapy_type")

admin.site.register(City, CityAdmin)
# Register your models here.
