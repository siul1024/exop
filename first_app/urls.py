from django.urls import path, include
from first_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('c1/', views.C1ListView.as_view(), name='c1_shop_list'),
    path('c2/', views.C2ListView.as_view(), name='c2_shop_list'),
]