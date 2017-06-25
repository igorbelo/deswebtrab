# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from forms import BookForm, DonationForm, SupplierForm, CustomerForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth import authenticate, login, logout

class BookView(SuccessMessageMixin, FormView):
    template_name = 'book.html'
    form_class = BookForm
    success_url = reverse_lazy('book')
    success_message = 'Solicitação enviada com sucesso!'

    def form_valid(self, form):
        form.save(commit=True)
        return super(BookView, self).form_valid(form)

class DonateView(SuccessMessageMixin, FormView):
    template_name = 'donate.html'
    form_class = DonationForm
    success_url = reverse_lazy('donate')
    success_message = 'Solicitação enviada com sucesso!'

    def form_valid(self, form):
        form.save(commit=True)
        return super(DonateView, self).form_valid(form)

class SupplierSignUpView(SuccessMessageMixin, FormView):
    template_name = 'supplier_signup.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_signup')
    success_message = 'Cadastro realizado com sucesso!'

    def form_valid(self, form):
        supplier = form.save(commit=False)
        user = User()
        user.set_password(form.data['password'])
        if form.data['cpf']:
            user.username = form.data['cpf']
        else:
            user.username = form.data['cnpj']

        with transaction.atomic():
            user.save()
            supplier.user = user
            supplier.save()

        return super(SupplierSignUpView, self).form_valid(form)

class CustomerSignUpView(SuccessMessageMixin, FormView):
    template_name = 'customer_signup.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_signup')
    success_message = 'Cadastro realizado com sucesso!'

    def form_valid(self, form):
        customer = form.save(commit=False)
        user = User()
        user.set_password(form.data['password'])
        user.username = form.data['cpf']

        with transaction.atomic():
            user.save()
            customer.user = user
            customer.save()

        return super(CustomerSignUpView, self).form_valid(form)

class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Credenciais inválidas")
            return render(request, "login.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
