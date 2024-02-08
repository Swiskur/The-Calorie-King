from django.contrib import admin

# Register your models here.
from .models import ApiData, CalorieResult, Macros

admin.site.register(ApiData)
admin.site.register(CalorieResult)
admin.site.register(Macros)