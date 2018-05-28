from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ['country', 'capital', 'language', 'habitants', 'continent', 'square_kilometers' ]

admin.site.register(Country, CountryAdmin)
