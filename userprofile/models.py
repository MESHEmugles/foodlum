from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




STATUS=[
    ('New','New'),
    ('Pending','Pending'),
    ('Process','Process'),
    ('closed','Closed')
]

class UContact(models.Model):
    # tailor your fields to what you have in the page file
    first_name= models.CharField(max_length=100, blank=True, null=True)
    last_name= models.CharField(max_length=100, blank=True, null=True)
    email= models.EmailField(max_length=100, blank=True, null=True)
    phone= models.CharField(max_length=100, blank=True, null=True)
    message= models.TextField(blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=100, choices=STATUS, default='new')
    closed= models.DateTimeField(blank=True, null=True )


    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'ucontact'
        managed = True
        verbose_name = 'UContact'
        verbose_name_plural = 'UContacts'


class UProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to ='profile', default='profile.jpg', blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    cart_code = models.AutoField(primary_key=True, serialize=True)

    def __str__(self):
        return self.user.username      
    
    class Meta:
        db_table = 'uprofile'
        managed = True
        verbose_name = 'UProfile'
        verbose_name_plural = 'UProfiles'