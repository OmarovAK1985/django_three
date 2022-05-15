from django.contrib import admin
from .import models


@admin.register(models.Phones)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'release_date')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'release_date')

# Register your models here.
