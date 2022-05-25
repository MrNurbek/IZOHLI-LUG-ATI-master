from django.contrib import admin

from main.models import *


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Word, WordAdmin)
