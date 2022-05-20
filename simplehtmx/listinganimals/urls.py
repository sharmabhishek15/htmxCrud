from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index' ),
    path('breed/', views.breed, name='breed'),
    path('add_animal/', views.addAnimal, name='add_animal'),
    path('delete_animal/<pk>', views.deleteAnimal, name='delete_animal'),
    path('admin/', admin.site.urls),
]