from django import forms
from django.forms import ModelForm, CharField, Textarea

from core.models import Reserva, Donation, Supplier, Customer

class BookForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ('remedio','quantity','quantity_unit','pills','doctor','crm','prescription')

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ('remedio','quantity','quantity_unit','pills','date')

class SupplierForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

    class Meta:
        model = Supplier
        fields = ('full_name','razao_social','cpf','cnpj','address','description')

class CustomerForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

    class Meta:
        model = Customer
        fields = ('full_name','mothers_name','birth_date','cpf','rg','address','sus')
