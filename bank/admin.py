from django.contrib import admin
from .models import CustomerProfile, NextOfKin, Transaction

# Register your models here.
admin.site.register(CustomerProfile)
admin.site.register(NextOfKin)
admin.site.register(Transaction)
