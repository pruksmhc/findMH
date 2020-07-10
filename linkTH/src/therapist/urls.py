from django.urls import path, include

# Import 'therapist' views
from .views import (
    therapist_detail_view,
    therapist_list_view,
    therapist_create_view,
    therapist_update_view,
    therapist_delete_view,
)

urlpatterns = [

    # Therapist app views
    path('', therapist_list_view),
    path('<int:th_id>/', therapist_detail_view),
    path('create/', therapist_create_view),
    path('<int:th_id>/update/', therapist_update_view),
    path('<int:th_id>/delete/', therapist_delete_view),
    # path('therapist/<str:slug>/', therapist_detail_page),

]

