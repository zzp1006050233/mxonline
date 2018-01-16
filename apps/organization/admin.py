from django.contrib import admin

# Register your models here.
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'descc']
    list_filter = ['add_time']


class CourseOrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'address']
    list_filter = ['click_nums', 'fav_nums', 'city', 'add_time']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'org', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'org', 'work_company', 'work_position']
    list_filter = ['work_years', 'click_nums', 'fav_nums', 'add_time']


admin.site.register(CityDict, CityDictAdmin)
admin.site.register(CourseOrg, CourseOrgAdmin)
admin.site.register(Teacher, TeacherAdmin)