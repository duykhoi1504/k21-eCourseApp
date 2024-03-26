from django.contrib import admin
from courses.models import  Category, Course
from django.utils.html import mark_safe
# Register your models here.

class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date','updated_date','active']
    search_fields = ['name']
    list_filter = ['id','created_date','name']
    readonly_fields = ['my_image']

    def my_image(self,instance):
        if instance:
            return mark_safe(f"<img width='400' src='/static/{instance.image.name}'/>")

    class Media:
        css={
            'all':('/static/css/style.css',)
    }

admin.site.register(Category)
admin.site.register(Course,MyCourseAdmin)