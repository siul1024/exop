
from django.shortcuts import render
from first_app.models import ShopInfo

# 함수로 사용하는 방법
# render를 사용해 dict로 전달
def index(request):
    all_count = ShopInfo.objects.all().count()
    # 분류별
    c1_count = ShopInfo.objects.filter(cat_id='1').count()
    c2_count = ShopInfo.objects.filter(cat_id='2').count()
    c3_count = ShopInfo.objects.filter(cat_id='3').count()
    c4_count = ShopInfo.objects.filter(cat_id='4').count()
    c5_count = ShopInfo.objects.filter(cat_id='5').count()
    c6_count = ShopInfo.objects.filter(cat_id='6').count()
    c7_count = ShopInfo.objects.filter(cat_id='7').count()
    c8_count = ShopInfo.objects.filter(cat_id='8').count()
    c9_count = ShopInfo.objects.filter(cat_id='9').count()
    # 건물별
    b1_count = ShopInfo.objects.filter(bldg_id='1').count()
    b2_count = ShopInfo.objects.filter(bldg_id='2').count()
    b3_count = ShopInfo.objects.filter(bldg_id='3').count()
    b4_count = ShopInfo.objects.filter(bldg_id='4').count()
    b5_count = ShopInfo.objects.filter(bldg_id='5').count()
    b6_count = ShopInfo.objects.filter(bldg_id='6').count()
    b7_count = ShopInfo.objects.filter(bldg_id='7').count()
    b8_count = ShopInfo.objects.filter(bldg_id='8').count()
    b9_count = ShopInfo.objects.filter(bldg_id='9').count()
    b10_count = ShopInfo.objects.filter(bldg_id='10').count()
    b11_count = ShopInfo.objects.filter(bldg_id='11').count()

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
        'b1_count': b1_count,
        'b2_count': b2_count,
        'b3_count': b3_count,
        'b4_count': b4_count,
        'b5_count': b5_count,
        'b6_count': b6_count,
        'b7_count': b7_count,
        'b8_count': b8_count,
        'b9_count': b9_count,
        'b10_count': b10_count,
        'b11_count': b11_count,
    }
    return render(request, 'index.html', context=context)