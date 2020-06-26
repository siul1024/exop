from django.urls import path
from first_app import view_cat
from first_app.view_index import index


urlpatterns = [
    path('', index, name='index'),

    path('c1/', view_cat.C1ListView.as_view(), name='c1_shop_list'),
    path('c2/', view_cat.C2ListView.as_view(), name='c2_shop_list'),
    path('c3/', view_cat.C3ListView.as_view(), name='c3_shop_list'),
    path('c4/', view_cat.C4ListView.as_view(), name='c4_shop_list'),
    path('c5/', view_cat.C5ListView.as_view(), name='c5_shop_list'),
    path('c6/', view_cat.C6ListView.as_view(), name='c6_shop_list'),
    path('c7/', view_cat.C7ListView.as_view(), name='c7_shop_list'),
    path('c8/', view_cat.C8ListView.as_view(), name='c8_shop_list'),
    path('c9/', view_cat.C9ListView.as_view(), name='c9_shop_list'),
]