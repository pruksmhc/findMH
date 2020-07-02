"""findTH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# For static files
from django.conf import settings
# For search engine
from searches.views import search_view

from .views import (
	home_page,
	about_page,
	contact_page,
	example_page
    )

from blog.views import (

    blog_post_create_view,

    )

urlpatterns = [
 	path('', home_page),
 	path('about/', about_page),
 	path('contact/', contact_page),
 	path('example/', example_page),
    path('admin/', admin.site.urls),

    # This view is firts because it searches top to bottom and stops at first
    # using /*-new/ cause '/create' could bring problems with slug
    path('blog-new/', blog_post_create_view),
    path('blog/', include('blog.urls')),

    # Search engine view
    path('search/', search_view),

]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
