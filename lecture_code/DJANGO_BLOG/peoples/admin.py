from django.contrib import admin

from .models import People

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'job', 'address')

admin.site.register(People, PeopleAdmin)

