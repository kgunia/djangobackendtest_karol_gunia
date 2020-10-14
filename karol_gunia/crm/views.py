from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Customer
from django.contrib import messages


# Create your views here.
class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Customer
    permission_required = 'crm.add_customer'
    fields = ['first_name','last_name', 'email', 'telephone']

    def form_valid(self, form):
        first_name = form.instance.first_name
        last_name = form.instance.last_name
        exists = Customer.objects.filter(first_name=first_name, last_name=last_name).first()
        if exists and form.instance.pk != exists.pk:
            messages.add_message(self.request, messages.INFO, f'Customer {first_name} {last_name} already exists')
            return super().form_invalid(form)
        else:
            return super().form_valid(form)

class CustomerUpdateView(CustomerCreateView, UpdateView):
    permission_required = 'crm.change_customer'

class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    permission_required = 'crm.delete_customer'

class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Customer
    permission_required = 'crm.view_customer'

    