from django.contrib import admin
from .models import News
# Register your models here.
@admin.register(News)

class AdminCreate(admin.ModelAdmin):
    list_display = ["id","title","date","nr","post"]
