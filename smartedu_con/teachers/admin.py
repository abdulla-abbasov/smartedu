from django.contrib import admin

from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)