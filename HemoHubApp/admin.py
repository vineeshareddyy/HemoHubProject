from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PersonData

@admin.register(PersonData)
class PersonDataAdmin(ImportExportModelAdmin):
    list_display= ('Person_Name','Blood_Type',  'Component','Quantity','Expiry_Date')
from django.apps import AppConfig


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

