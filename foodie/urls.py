from django.urls import path
from . import views




urlpatterns=[
    path('', views.index, name='index'),
    path('meals/', views.meals, name='meals'),
    path('searched/', views.searched, name='searched'),
    path('meal/<str:id>/<str:slug>', views.meal, name='meal'),    
    path('varieties/<str:id>/<str:slug>', views.varieties, name='varieties'),
    path('loggin/', views.loggin, name='loggin'),
    # path('singin/', views.signin, name='signin'),
    path('loggout/', views.loggout, name='loggout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('contactus/', views.contactus, name='contactus'),
    path('profileupdate/', views.profileupdate, name='profileupdate'),
    path('password_recovery/', views.password_recovery, name='password_recovery'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('remove_item/', views.remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('paid_order/', views.paid_order, name='paid_order'),
    path('paidorder/', views.paidorder, name='paidorder'),
    # 
]