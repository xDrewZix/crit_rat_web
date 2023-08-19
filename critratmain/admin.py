from django.contrib import admin

# Register your models here.

from .models import Main, CritRats

admin.site.register(Main)
admin.site.register(CritRats)
