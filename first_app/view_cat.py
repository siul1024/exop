
# Create your views here.
from django.views.generic import ListView
from first_app.models import ShopInfo #, BuildingInfo, Category


# 클래스로 사용하는 방법, (제너릭 보기 뷰, generic display view)
class C1ListView(ListView):
    #join(select_related), 컬럼명__컬럼명
    # 쿼리셋 사용시 model속성은 무시됨
    # model = ShopInfo.objects.filter(cat_id__cat_name='한식').values('shop_name','bldg')
    context_object_name = 'c1_shop_list'
    queryset = ShopInfo.objects.filter(cat_id__cat_name='한식')[:]
    template_name = 'c_shop/c1_shop_list.html'

    # def get_queryset(self):
    #     return ShopInfo.objects.filter(cat_id__cat_name='한식')[:]

    def get_context_data(self, *, object_list=None, **kwargs):
        # 수퍼클래스에서 기존 context를 가져옴
        context = super(C1ListView, self).get_context_data(**kwargs)
        # 새로운 컨텍스트 정보 추가
        context['some_data'] = 'just some data'
        return context


class C2ListView(ListView):
    context_object_name = 'c2_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=2)[:]
    template_name = 'c_shop/c2_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C2ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C3ListView(ListView):
    context_object_name = 'c3_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=3)[:]
    template_name = 'c_shop/c3_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C3ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C4ListView(ListView):
    context_object_name = 'c4_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=4)[:]
    template_name = 'c_shop/c4_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C4ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C5ListView(ListView):
    context_object_name = 'c5_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=5)[:]
    template_name = 'c_shop/c5_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C5ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C6ListView(ListView):
    context_object_name = 'c6_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=6)[:]
    template_name = 'c_shop/c6_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C6ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C7ListView(ListView):
    context_object_name = 'c7_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=7)[:]
    template_name = 'c_shop/c7_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C7ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C8ListView(ListView):
    context_object_name = 'c8_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=8)[:]
    template_name = 'c_shop/c8_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C8ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class C9ListView(ListView):
    context_object_name = 'c9_shop_list'
    queryset = ShopInfo.objects.filter(cat_id=9)[:]
    template_name = 'c_shop/c9_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C9ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context
