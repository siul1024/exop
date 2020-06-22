from django.urls import path, include
from first_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('c1/', views.C1ListView.as_view(), name='c1_shop_list'),
    path('c2/', views.C2ListView.as_view(), name='c2_shop_list'),
    path('c3/', views.C3ListView.as_view(), name='c3_shop_list'),
    path('c4/', views.C4ListView.as_view(), name='c4_shop_list'),
    path('c5/', views.C5ListView.as_view(), name='c5_shop_list'),
    path('c6/', views.C6ListView.as_view(), name='c6_shop_list'),
    path('c7/', views.C7ListView.as_view(), name='c7_shop_list'),
    path('c8/', views.C8ListView.as_view(), name='c8_shop_list'),
    path('c9/', views.C9ListView.as_view(), name='c9_shop_list'),
]