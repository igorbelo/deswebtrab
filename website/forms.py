from django import forms
from django.forms import ModelForm, CharField, Textarea

from core.models import Reserva, Donation

class BookForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ('remedio','quantity','quantity_unit','pills','doctor','crm','prescription')

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ('remedio','quantity','quantity_unit','pills','date')
