from django.shortcuts import render

# Create your views here.

from first_app.models import Category, BuildingInfo, ShopInfo

def index(request):
    s_count = ShopInfo.objects.all().count()
    korean_count = ShopInfo.objects.filter(cat_id='1').count()

    context = {
        's_count': s_count,
        'korean_count': korean_count,
    }

    return render(request, 'index.html', context=context)