from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import \
    (ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView)
from .models import Nonconformity


# Class based view for home page

class NonconformityListView(ListView):
    model = Nonconformity
    template_name = 'nonconformity/home.html'
    context_object_name = 'nonconformity_list'
    ordering = ['-occ_date']


class NonconformityDetailView(DetailView):
    model = Nonconformity


class NonconformityCreateView(CreateView):
    model = Nonconformity
    fields = ['description', 'type', 'occ_date', 'employee']


class NonconformityUpdateView(UpdateView):
    model = Nonconformity
    fields = ['description', 'type', 'occ_date', 'employee']


class NonconformityDeleteView(DeleteView):
    model = Nonconformity
