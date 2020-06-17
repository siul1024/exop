from django.shortcuts import render

# Create your views here.

from first_app.models import Category, BuildingInfo, ShopInfo

def index(request):
    all_count = ShopInfo.objects.all().count()
    c1_count = ShopInfo.objects.filter(cat_id='1').count()
    c2_count = ShopInfo.objects.filter(cat_id='2').count()
    c3_count = ShopInfo.objects.filter(cat_id='3').count()
    c4_count = ShopInfo.objects.filter(cat_id='4').count()
    c5_count = ShopInfo.objects.filter(cat_id='5').count()
    c6_count = ShopInfo.objects.filter(cat_id='6').count()
    c7_count = ShopInfo.objects.filter(cat_id='7').count()
    c8_count = ShopInfo.objects.filter(cat_id='8').count()
    c9_count = ShopInfo.objects.filter(cat_id='9').count()


    context = {
        'all_count': all_count,
        'c1_count': c1_count,
        'c2_count': c2_count,
        'c3_count': c3_count,
        'c4_count': c4_count,
        'c5_count': c5_count,
        'c6_count': c6_count,
        'c7_count': c7_count,
        'c8_count': c8_count,
        'c9_count': c9_count,
    }

    return render(request, 'index.html', context=context)