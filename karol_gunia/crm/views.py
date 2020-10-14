from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Customer, Purchase
from django.contrib import messages
from .forms import CarForm


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
            messages.add_message(self.request, messages.INFO, f'Saved')
            return super().form_valid(form)

class CustomerUpdateView(CustomerCreateView, UpdateView):
    permission_required = 'crm.change_customer'

class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    permission_required = 'crm.delete_customer'
    success_url = '/customer/'


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Customer
    permission_required = 'crm.view_customer'

    def get_queryset(self):
        product = self.request.GET.get('product', None)
        if product:
            return super().get_queryset().filter(purchase__product=product).distinct()
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarForm(self.request.GET)
        return context

class PurchaseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Purchase
    fields = ['customer', 'product']
    permission_required = 'crm.add_purchase'

class PurchaseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Purchase
    permission_required = 'crm.view_purchase'

    def get_queryset(self):
        product = self.request.GET.get('product', None)
        if product:
            return super().get_queryset().filter(product=product)
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarForm(self.request.GET)
        return context