from shopcart.models import Shopcart
from foodie.models import Variety
# from userprofile.models import UProfile




# def imagecl(request):
#     profile = UProfile.objects.get(user__username= request.user.username)

#     context={
#         'profile':profile
#     }

#     return context

    

def dropdown(request):
    variety= Variety.objects.all()

    
    context={
        'variety':variety
    }

    return context


def cartpros(request):
    carty= Shopcart.objects.filter(user__username = request.user.username, item_paid=False)

    cartcount = 0
    
    for item in carty:
        cartcount += item.quantity
    
    context ={
        'cartcount':cartcount,
    }

    return context
