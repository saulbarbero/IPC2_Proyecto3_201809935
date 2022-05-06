from django.contrib import admin
from . import models

# Register your models here.

class InfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Prueba,InfoAdmin)
