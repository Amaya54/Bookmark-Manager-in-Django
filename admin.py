from django.contrib import admin
from .models import *
# Register your models here.
class employee1 (admin.ModelAdmin):
    list_per_page = 100
    
admin.site.register(bookmark,employee1)

