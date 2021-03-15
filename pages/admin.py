from django.contrib import admin

from . import models

@admin.register(models.Stats)
class Stat(admin.ModelAdmin):
    list_display = ("querystring", "amount")
    search_fields = ("querystring__startswith", )
# Register your models here.
