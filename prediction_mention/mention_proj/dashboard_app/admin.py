from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'maths', 'français', 'philosophie', 'physique', 'mention')

admin.site.register(Data, DataAdmin)