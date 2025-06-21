from django.urls import path, include

from petstagram_two.photos import views

urlpatterns = [
    path('add/', views.PhotoAddView.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsView.as_view(), name='photo-details'),
        path('edit/', views.PhotoEditView.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ]))
]