from re import M
from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Variety(models.Model):
    name= models.CharField(max_length=100)
    slug= models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to= 'variety', default='variety.jpg', blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    

    # this is not compulsory(it's just to show the table in the specific name chosen)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'variety'
        managed = True
        verbose_name = 'Variety'
        verbose_name_plural = 'Varieties'
    





class Meal(models.Model):
    variety= models.ForeignKey(Variety, on_delete=models.CASCADE)
    meal = models.CharField(max_length=100)
    slug= models.SlugField(unique=True, null=False)
    image= models.ImageField(upload_to= 'meal', default='meal.jpg', blank=True, null=True)
    #choices works with list containing turples
    menu = models.TextField()
    min_order = models.IntegerField(default=1)
    max_order = models.IntegerField(default=10)  
    time = models.CharField(max_length=100)
    # info = models.CharField(max_length=100, default='o')
    # infos = models.CharField(max_length=100, default='o')
    # inffo = models.CharField(max_length=100, default='o')
    price= models.IntegerField()
    discount= models.FloatField()
    breakfast= models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()
    display= models.BooleanField()
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    



    def __str__(self):
        return self.meal

    class Meta:
        db_table = 'meal'
        managed = True
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'








