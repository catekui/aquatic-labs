from django.contrib import admin

# Register your models here.
from . models import Blog, Publications


admin.site.register(Blog)
admin.site.register(Publications) 