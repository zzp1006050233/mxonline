from django.contrib import admin

# Register your models here.
from .models import UserAsk, CourseComment,  UserFavorite, UserMessage, UserCourse


class UserAskAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_name', 'add_time']
    search_fields = ['name', 'course_name']
    list_filter = ['course_name', 'add_time']


class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comments', 'course', 'add_time']
    search_fields = ['name', 'comments']
    list_filter = ['course', 'add_time']


class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'fav_id', 'add_time']
    search_fields = ['fav_id']
    list_filter = ['add_time']


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message']
    list_filter = ['has_read', 'add_time']


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user']
    list_filter = ['course', 'add_time']


admin.site.register(UserAsk, UserAskAdmin)
admin.site.register(CourseComment, CourseCommentAdmin)
admin.site.register(UserFavorite, UserFavoriteAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(UserCourse, UserCourseAdmin)