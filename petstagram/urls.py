
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('acount/', include('petstagram.accounts.urls')),
    path('pet/', include('petstagram.pets.urls')),
    path('photo/', include('petstagram.photos.urls')),
]