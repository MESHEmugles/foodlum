from django.contrib import admin
from .models import *

# Register your models here.

class VarietyAdmin(admin.ModelAdmin):
    list_display=('id','name','slug','image','created','updated')
    list_display_links = ('id','name','slug')
    prepopulated_fields = {'slug': ('name',)}

    

admin.site.register(Variety, VarietyAdmin)



class MealAdmin(admin.ModelAdmin):
    list_display = ('id','variety','meal','slug','image','menu','display','time','min_order','max_order','price','breakfast','lunch','dinner','updated','discount')
    list_display_links = ('id','variety','meal','slug')
    prepopulated_fields = {'slug': ('meal',)}
    list_editable= ['display','discount']

admin.site.register(Meal, MealAdmin)





