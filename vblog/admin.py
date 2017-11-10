from django.contrib import admin
from .models import Category, Tag, Blog

# class User_admin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'validate')
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
