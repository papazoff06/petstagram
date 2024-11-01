from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('', views.pet_add_page,  name='pet_add_page'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pet_details_page'),
        path('edit/', views.pet_edit_page, name='pet_edit_page'),
        path('delete/', views.pet_delete_page, name='pet_delete_page'),
    ])),
]