# use for user to create an account of theirs
from dataclasses import field
from logging import PlaceHolder
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.forms import ModelForm
from userprofile.models import UContact, UProfile
from shopcart.models import *





class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)



    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']



class ContactForm(forms.ModelForm):
    class Meta:
        model = UContact
        fields = ['first_name', 'last_name','email', 'phone', 'message']


STATE=[
    ('Abia', 'Abia'),
    ('Abuja', 'Abuja'),
    ('Edo', 'Edo'),
    ('Kano', 'Kano'),
    ('Lagos', 'Lagos'),
    ('Ogun', 'Ogun'),
    ('Ph', 'Ph'),
]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UProfile
        fields = ['first_name', 'last_name','email', 'phone','address','city','zip','state', 'image']
        widgets ={
            'first_name': forms.TextInput(attrs={'class':'pe', 'PlaceHolder':'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'pe', 'placeholder':'last_name'}),
            'phone': forms.TextInput(attrs={'class':'pe', 'placeholder':'phone'}),
            'email': forms.EmailInput(attrs={'class':'pe', 'placeholder':'email'}),
            'address': forms.TextInput(attrs={'class':'pe', 'placeholder':'address'}),
            'state': forms.Select(attrs={'class':'pe', 'placeholder':'state'}, choices=STATE),
            'image': forms.FileInput(attrs={'placeholder':'upload image file'}),
            'city': forms.TextInput(attrs={'class':'pe', 'PlaceHolder':'city'}),
            'zip': forms.NumberInput(attrs={'class':'pe', 'PlaceHolder':'zip'}),
        }


class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart
        fields= ['quantity','now_spicy', 'product_name']



