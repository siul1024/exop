from django.urls import path, include
from first_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('c1/', views.C1ListView.as_view(), name='c1_shop_list')
]