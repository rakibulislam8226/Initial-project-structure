from django.contrib import admin
from axes.admin import AccessLog


def show_blocked_users(modeladmin, request, queryset):
    blocked_users = AccessLog.objects.filter(response_code__in=[401, 403])
    blocked_usernames = blocked_users.values_list('username', flat=True).distinct()
    blocked_user_list = ", ".join(blocked_usernames)
    message = f"Blocked Users: {blocked_user_list}"
    modeladmin.message_user(request, message)

show_blocked_users.short_description = "Show Blocked Users"

class AccessLogAdmin(admin.ModelAdmin):
    actions = [show_blocked_users] 

admin.site.unregister(AccessLog) 
admin.site.register(AccessLog, AccessLogAdmin)
