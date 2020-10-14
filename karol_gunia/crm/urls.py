from django.urls import path
from django.views.generic import RedirectView
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

urlpatterns = [

    path('', RedirectView.as_view(pattern_name='customer-list', permanent=False)),
    path('customer/', CustomerListView.as_view(), name='customer-list'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),

]
