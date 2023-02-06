from django.contrib import admin
from . models import *
# Register your models here.

@admin.register((Person))
class personModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','msg']
    
@admin.register((Product))
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name','description','img']