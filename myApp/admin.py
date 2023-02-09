from django.contrib import admin
from myApp.models import FileHandler


@admin.register(FileHandler)
class FileHandlerAdmin(admin.ModelAdmin):
    """FileHandler"""

