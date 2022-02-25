from django.contrib import admin
from .models import Category,Product,profile,Review,ContactUs,order
# Register your models here.
admin.site.site_header = "Suke Adminstration"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','product_category','image','product_created_date','product_updated_date')
    list_filter = ['name','price','product_category']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_created_date','category_updated_date')
    list_filter = ['category_name','category_created_date','category_updated_date']
    search_fields = ['category_name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Orderd_by','Grand_total','Payment_method','Orderd_date')
    list_filter = ['First_name','Orderd_date','Payment_method']
    search_fields = ['First_name','Payment_Method','orderd_by']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(profile)
admin.site.register(Review)
admin.site.register(ContactUs)
admin.site.register(order,OrderAdmin)


