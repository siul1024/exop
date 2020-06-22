from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from first_app.models import ShopInfo #, BuildingInfo, Category

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


# 클래스로 사용하는 방법
class C1ListView(ListView):
    #join(select_related), 컬럼명__컬럼명
    model = ShopInfo.objects.filter(cat_id__cat_name='한식').values('shop_name','bldg')
    context_object_name = 'c1_shop_list'
    queryset = ShopInfo.objects.filter(cat_id__cat_name='한식')[:]
    template_name = 'c_shop/c1_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id__cat_name='한식')[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        # 수퍼클래스에서 기존 context를 가져옴
        context = super(C1ListView, self).get_context_data(**kwargs)
        # 새로운 컨텍스트 정보 추가
        context['some_data'] = 'just some data'
        return context


class C2ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=2).values('shop_name','bldg')
    context_object_name = 'c2_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=2)[:]
    template_name = 'c_shop/c2_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=2)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C2ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C3ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=3).values('shop_name','bldg')
    context_object_name = 'c3_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=3)[:]
    template_name = 'c_shop/c3_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=3)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C3ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C4ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=4).values('shop_name','bldg')
    context_object_name = 'c4_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=4)[:]
    template_name = 'c_shop/c4_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=4)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C4ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C5ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=5).values('shop_name','bldg')
    context_object_name = 'c5_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=5)[:]
    template_name = 'c_shop/c5_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=5)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C5ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C6ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=6).values('shop_name','bldg')
    context_object_name = 'c6_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=6)[:]
    template_name = 'c_shop/c6_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=6)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C6ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C7ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=7).values('shop_name','bldg')
    context_object_name = 'c7_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=7)[:]
    template_name = 'c_shop/c7_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=7)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C7ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C8ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=8).values('shop_name','bldg')
    context_object_name = 'c8_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=8)[:]
    template_name = 'c_shop/c8_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=8)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C8ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C9ListView(ListView):
    model = ShopInfo.objects.filter(cat_id=9).values('shop_name','bldg')
    context_object_name = 'c9_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=9)[:]
    template_name = 'c_shop/c9_shop_list.html'

    def get_queryset(self):
        return ShopInfo.objects.filter(cat_id=9)[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C9ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context
