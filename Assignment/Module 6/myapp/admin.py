from django.contrib import admin
from .models import *
# Register your models here.
class adminModel(admin.ModelAdmin):
    model=BookModel
    list_display=['title','author','isbn','publisher']
admin.site.register(BookModel,adminModel)