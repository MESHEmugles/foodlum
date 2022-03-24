from django.db import models
from django.contrib.auth.models import User
from foodie.models import Meal

# Create your models here.



class Shopcart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    meal= models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    now_spicy=models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    total= models.IntegerField(default=1)
    order_no= models.CharField(max_length=50)
    item_paid= models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'shopcart'
        managed = True
        verbose_name = 'Shopcart'
        verbose_name_plural = 'Shopcarts'


STATUS = [
    ('New','New'),
    ('Pending','Pending'),
    ('Processing','Processing'),
    ('Shipping','Shipping'),
    ('Delivered','Delivered'),
]
class Checkout(models.Model):
    shopcart= models.ForeignKey(Shopcart, on_delete=models.CASCADE)
    ordr_no= models.CharField(max_length=50)
    itm_paid= models.BooleanField(default=False)
    total= models.FloatField()
    address= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    zip= models.IntegerField()
    name_on_card= models.CharField(max_length=200)
    card_number= models.IntegerField()
    cvv= models.IntegerField()
    month= models.CharField(max_length=50)
    status = models.CharField(max_length = 50, choices=STATUS)
    admin_remark= models.CharField(max_length=250)
    

    def __str__(self):
        return self.shopcart.user.username


    class Meta:
        db_table = 'checkout'
        managed = True
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'


class Paidorder(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=50)
    paid_item = models.BooleanField(default=False)
    name_on_crd= models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'paidorder'
        managed = True
        verbose_name = 'Paidorder'
        verbose_name_plural = 'Paidorders'


class Ship(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    meal= models.ForeignKey(Meal, on_delete=models.CASCADE,blank=True, null=True)
    ordr_no= models.CharField(max_length=36, blank=True, null=True)
    itm_paid= models.BooleanField(default=False)
    phone= models.CharField(max_length=20,blank=True, null=True)
    total= models.FloatField()
    address= models.CharField(max_length=50,blank=True, null=True)
    state= models.CharField(max_length=50,blank=True, null=True)
    name_on_crd= models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.user.username