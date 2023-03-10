from django.contrib import admin
from . models import *

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(Plan, PlanAdmin)