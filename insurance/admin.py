from django.contrib import admin
from .models import *

# Register your models here.

class cat(admin.ModelAdmin):
    list_display = ['id','category_name','creation_date']
admin.site.register(Category,cat)

class pol(admin.ModelAdmin):
    list_display = ['id','category','policy_name','sum_assurance','premium','tenure','creation_date']
admin.site.register(Policy,pol)

class polrec(admin.ModelAdmin):
    list_display = ['id','customer','Policy','status','creation_date']
admin.site.register(PolicyRecord,polrec)

class que(admin.ModelAdmin):
    list_display = ['id','customer','description','admin_comment','asked_date']
admin.site.register(Question,que)

admin.site.register(contact)