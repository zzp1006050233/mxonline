__author__ = 'zzp'
__date__ = '2018/1/15 10:57'


from django.urls import path, include
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeachersView, AddFavView


urlpatterns = [
    # 课程机构
    path('list', OrgView.as_view(), name="org_list"),
    path('add_ask', AddUserAskView.as_view(), name="add_ask"),
    path('home/<int:org_id>', OrgHomeView.as_view(), name="org_home"),
    path('course/<int:org_id>', OrgCourseView.as_view(), name="org_course"),
    path('desc/<int:org_id>', OrgDescView.as_view(), name="org_desc"),
    path('teachers/<int:org_id>', OrgTeachersView.as_view(), name="org_teachers"),

    # 机构收藏
    path('add_fav', AddFavView.as_view(), name='add_fav')

]

app_name = 'org'
