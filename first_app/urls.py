from django.urls import path, include
from first_app import views


urlpatterns = [
    path('', views.index, name='index'),
]