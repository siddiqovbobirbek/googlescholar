from django.contrib import admin
from myApp.models import FileHandler, Certificate, Article, Book, Dissertation


@admin.register(FileHandler)
class FileHandlerAdmin(admin.ModelAdmin):
    """FileHandler"""

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "muallif", "data", "dgunomer")
    list_display_links = ("muallif", "dgunomer")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "muallif", "journal_name", "nashr_sanasi")
    list_display_links = ("muallif", "journal_name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "muallif", "nashr_sanasi", "nashriyot_name")
    list_display_links = ("name", "muallif")


@admin.register(Dissertation)
class DissertationAdmin(admin.ModelAdmin):
    list_display = ("name", "muallif", "yunalish")
    list_display_links = ("name", "muallif", "yunalish")
