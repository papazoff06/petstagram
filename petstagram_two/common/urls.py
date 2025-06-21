from django.urls import path

from petstagram_two.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.copy_linc_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment'),
]