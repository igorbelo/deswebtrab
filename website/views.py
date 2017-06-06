# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView
from forms import BookForm, DonationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

class BookView(FormView):
    template_name = 'book.html'
    form_class = BookForm
    success_url = reverse_lazy('book')

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'Solicitação enviada com sucesso!')
        return super(BookView, self).form_valid(form)

class DonateView(FormView):
    template_name = 'donate.html'
    form_class = DonationForm
    success_url = reverse_lazy('donate')

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'Solicitação enviada com sucesso!')
        return super(DonateView, self).form_valid(form)
