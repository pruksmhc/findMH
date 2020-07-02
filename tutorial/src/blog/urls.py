from django.urls import path

from .views import (
    blog_post_detail_view,
    # blog_post_detail_page,
    blog_post_update_view,
    blog_post_delete_view,
    blog_post_list_view,
    blog_post_create_view,

    )

urlpatterns = [
    # path('blog/<int:post_id>/', blog_post_detail_page_id),
    path('', blog_post_list_view),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
    # using /*-new/ cause '/create' could bring problems with slug
    #path('blog-new/', blog_post_create_view),
] 

from django.conf import settings

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
