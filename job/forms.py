from django.contrib.auth.models import User
from django import forms
from .models import Offer, MPTTModel, Category
from mptt.forms import *


class OfferRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    price = forms.DecimalField(required=True)
    start_time = forms.DateField(required=False)
    end_time = forms.DateField(required=False)
    description = forms.Textarea()
    # category = TreeNodeChoiceField(queryset=Category.objects.filter(is_active=True))
    image = forms.ImageField(required=False)

    class Meta:
        model = Offer
        fields = ('first_name', 'last_name', 'middle_name', 'phone', 'email', 'name', 'image', 'description', 'price', 'start_time', 'end_time')
        exclude = ['created', 'updated', 'category']
