from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from .forms import *
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import CustomerProfileForm
from .models import CustomerProfile
# Create your views here.

def banking_page(request):
    return render(request, 'bank/home.html')



class CreateCustomer(SuccessMessageMixin, CreateView):
    template_name = 'bank/customer_registration.html'
    model = CustomerProfile
    form_class = CustomerProfileForm
    success_url = 'customer-profile'
    success_message = "%(first_name) was created successfully"


def customer_profile(request):
    customer = CustomerProfile.objects.all()
    args = {'customer': customer}
    return render(request, 'bank/customer_profile.html', args)
