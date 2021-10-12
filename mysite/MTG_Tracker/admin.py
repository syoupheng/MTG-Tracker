from django.contrib import admin
from .models import DraftResult, Expansion

# Register your models here.
admin.site.register(Expansion)
admin.site.register(DraftResult)