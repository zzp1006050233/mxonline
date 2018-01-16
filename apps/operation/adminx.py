__author__ = 'zzp'
__date__ = '2018/1/9 17:28'

import xadmin

from .models import UserAsk, CourseComment,  UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'course_name', 'add_time']
    search_fields = ['name', 'course_name']
    list_filter = ['course_name', 'add_time']


class CourseCommentAdmin(object):
    list_display = ['user', 'comments', 'course', 'add_time']
    search_fields = ['name', 'comments']
    list_filter = ['course', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'add_time']
    search_fields = ['fav_id']
    list_filter = ['add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message']
    list_filter = ['has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user']
    list_filter = ['course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)