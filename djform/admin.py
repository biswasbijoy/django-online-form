from django.contrib import admin
from djform.models.models import FormModel


@admin.register(FormModel)
class FormAdmin(admin.ModelAdmin) :
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address']