from django.contrib import admin
from .models import *

# Register your models here.
class cust(admin.ModelAdmin):
    list_display = ['id','user','profile_pic','address','mobile']

admin.site.register(Customer,cust)