from django.contrib import admin

# Register your models here.

from .models import UserProfile, EmailVerifyRecord, Banner


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'nick_name']


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'add_time', 'index']
    search_fields = ['title']
    list_filter = ['title', 'add_time']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(Banner, BannerAdmin)
