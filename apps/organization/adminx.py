__author__ = 'zzp'
__date__ = '2018/1/9 17:53'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'descc']
    list_filter = ['add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'address']
    list_filter = ['click_nums', 'fav_nums', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'org', 'work_company', 'work_position']
    list_filter = ['work_years', 'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)