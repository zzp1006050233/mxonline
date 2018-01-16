__author__ = 'zzp'
__date__ = '2018/1/9 17:04'

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name']
    list_filter = ['degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']


class LessonAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)