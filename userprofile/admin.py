from django.contrib import admin
from . models import *

# Register your models here.



class UContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email', 'phone','message','created','status','closed')

admin.site.register(UContact, UContactAdmin)


class UProfileAdmin(admin.ModelAdmin):
    list_display = ('cart_code','user','first_name','last_name','email','phone', 'address','state','image')

admin.site.register(UProfile, UProfileAdmin)
