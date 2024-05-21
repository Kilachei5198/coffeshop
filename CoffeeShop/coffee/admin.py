from django.contrib import admin
from .models import coffee


class coffeeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')
admin.site.register(coffee, coffeeAdmin)
 