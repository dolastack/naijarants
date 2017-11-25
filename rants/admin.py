from django.contrib import admin
from .models import Rant
# Register your models here.

class RantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rant)
