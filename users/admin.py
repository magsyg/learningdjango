from django.contrib import admin

# Register your models here.
from .models import User, Section

admin.site.register(User)
admin.site.register(Section)