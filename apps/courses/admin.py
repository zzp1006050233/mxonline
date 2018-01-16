from django.contrib import admin

# Register your models here.
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name']
    list_filter = ['degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseResource, CourseResourceAdmin)