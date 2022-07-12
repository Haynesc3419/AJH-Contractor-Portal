from django.contrib import admin
from . import models
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth.models import User

# Register your models here.
class AssignmentsAdmin(admin.ModelAdmin):
    # title of note on list (tuple)
    list_display = ('date','company','patient')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Assignment, AssignmentsAdmin)
admin.site.register(models.Company, CompanyAdmin)