from django.urls import path
from first_app import view_cat, view_bldg
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

    path('b01/', view_bldg.B01ListView.as_view(), name='b01_shop_list'),
    path('b02/', view_bldg.B02ListView.as_view(), name='b02_shop_list'),
    path('b03/', view_bldg.B03ListView.as_view(), name='b03_shop_list'),
    path('b04/', view_bldg.B04ListView.as_view(), name='b04_shop_list'),
    path('b05/', view_bldg.B05ListView.as_view(), name='b05_shop_list'),
    path('b06/', view_bldg.B06ListView.as_view(), name='b06_shop_list'),
    path('b07/', view_bldg.B07ListView.as_view(), name='b07_shop_list'),
    path('b08/', view_bldg.B08ListView.as_view(), name='b08_shop_list'),
    path('b09/', view_bldg.B09ListView.as_view(), name='b09_shop_list'),
    path('b10/', view_bldg.B10ListView.as_view(), name='b10_shop_list'),
    path('b11/', view_bldg.B11ListView.as_view(), name='b11_shop_list'),
]