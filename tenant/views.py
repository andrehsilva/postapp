from django.shortcuts import render
from .models import Tenant
from django.contrib import messages
from django.db.models import Q

def tenant(request):
    tenants = Tenant.objects.all()
