from django.contrib import admin

from .models import WePynaire


@admin.register(WePynaire)
class WePynaireAdmin(admin.ModelAdmin):
    list_display = ("title", "start_datetime", "duration")
