
from django.views.generic import ListView
from first_app.models import ShopInfo #, BuildingInfo, Category


class B01ListView(ListView):
    context_object_name = 'b01_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=1)[:]
    template_name = 'b_shop/b01_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B01ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B02ListView(ListView):
    context_object_name = 'b02_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=2)[:]
    template_name = 'b_shop/b02_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B02ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B03ListView(ListView):
    context_object_name = 'b03_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=3)[:]
    template_name = 'b_shop/b03_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B03ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B04ListView(ListView):
    context_object_name = 'b04_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=4)[:]
    template_name = 'b_shop/b04_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B04ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B05ListView(ListView):
    context_object_name = 'b05_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=5)[:]
    template_name = 'b_shop/b05_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B05ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B06ListView(ListView):
    context_object_name = 'b06_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=6)[:]
    template_name = 'b_shop/b06_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B06ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B07ListView(ListView):
    context_object_name = 'b07_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=7)[:]
    template_name = 'b_shop/b07_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B07ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B08ListView(ListView):
    context_object_name = 'b08_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=8)[:]
    template_name = 'b_shop/b08_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B08ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B09ListView(ListView):
    context_object_name = 'b09_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=9)[:]
    template_name = 'b_shop/b09_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B09ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B10ListView(ListView):
    context_object_name = 'b10_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=10)[:]
    template_name = 'b_shop/b10_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B10ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context


class B11ListView(ListView):
    context_object_name = 'b11_shop_list'
    queryset = ShopInfo.objects.filter(bldg_id=11)[:]
    template_name = 'b_shop/b11_shop_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(B11ListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context

