from django.contrib import admin
from .models import HomeetUser


class HomeetUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'tg', 'sex', 'date_of_birth', 'who_are_you') 
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(HomeetUser, HomeetUserAdmin)