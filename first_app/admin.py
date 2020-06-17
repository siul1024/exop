from django.contrib import admin

# Register your models here.
from first_app.models import Category, BuildingInfo, ShopInfo


# category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'cat_name')

admin.site.register(Category, CategoryAdmin)


# building_info
class BuildingInfoAdmin(admin.ModelAdmin):
    list_display = ('bldg_id', 'bldg_name', 'bldg_lat', 'bldg_lng')

admin.site.register(BuildingInfo, BuildingInfoAdmin)


# shop_info
class ShopInfoAdmin(admin.ModelAdmin):
    list_display = ('shop_id', 'shop_name', 'bldg_id', 'cat_id', 'shop_tel')

admin.site.register(ShopInfo, ShopInfoAdmin)