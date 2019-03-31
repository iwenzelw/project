from django import forms
from .models import *

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'

class apartmentForm(forms.ModelForm):
    class Meta:
        model = apartment
        fields = ('title', 'text', 'price',)

class rentalForm(forms.ModelForm):
    class Meta:
        model = rental
        fields = ('title', 'text',)