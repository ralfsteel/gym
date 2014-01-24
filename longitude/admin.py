from django.contrib import admin
from longitude.models import Brand, Location


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )


class LocationAdmin(admin.ModelAdmin):
    list_display = ('brand', 'address', 'postal_code','postal_area','opening_hours')
    list_filter = ('brand', )


# Register your models here.

admin.site.register(Brand, BrandAdmin)
admin.site.register(Location, LocationAdmin)

