from django.contrib import admin
from .models import *

# Register your models here.


class ShopcartAdmin(admin.ModelAdmin):
    list_display = ('user','meal','now_spicy','product_name','quantity','total','order_no','item_paid')
    list_display_links= ('user','meal','product_name','quantity')
    readonly_fields =('user','meal','now_spicy','product_name','quantity','total','order_no','item_paid')
admin.site.register(Shopcart, ShopcartAdmin)

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('shopcart','ordr_no','itm_paid','total','address','state','city','zip','name_on_card','card_number','cvv','month','status','admin_remark',)
    list_display_links = ('shopcart','ordr_no', 'itm_paid')
    readonly_fields = ('shopcart','ordr_no','itm_paid','total','address','state','city','zip','name_on_card','card_number','cvv','month')

admin.site.register(Checkout, CheckoutAdmin)

class PaidorderAdmin(admin.ModelAdmin):
    list_display = ('id','user','total','cart_no','payment_code','paid_item','name_on_crd')
    list_display_links = ('id','user','cart_no','paid_item')
    readonly_fields = ('id','user','total','cart_no','payment_code','paid_item','name_on_crd')

admin.site.register(Paidorder, PaidorderAdmin)

class ShipAdmin(admin.ModelAdmin):
    list_display = ('id','user','total','ordr_no','itm_paid','name_on_crd','meal','address','state','name_on_crd','phone')
    list_disply_links = ('id','user','mel')
    redonly_fields = ('id','user','total','ordr_no','itm_paid','name_on_crd','meal','address','state','name_on_crd','phone')

admin.site.register(Ship, ShipAdmin)