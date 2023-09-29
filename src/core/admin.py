from django.contrib import admin
from axes.admin import AccessLog
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "uid",
        "phone",
        "first_name",
        "last_name",
        "email",
        "slug",
    ]
    list_filter = UserAdmin.list_filter + ("status",)
    readonly_fields = ("slug",)
    ordering = ("-date_joined",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Extra Fields",
            {
                "fields": (
                    "phone",
                    "slug",
                    "image",
                    "gender",
                    "type",
                    "status",
                    "date_of_birth",
                    "height",
                    "weight",
                    "blood_group",
                    "nid",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "phone",
                )
            },
        ),
    ) + UserAdmin.add_fieldsets


# Block user identifiers
def show_blocked_users(modeladmin, request, queryset):
    blocked_users = AccessLog.objects.filter(response_code__in=[401, 403])
    blocked_usernames = blocked_users.values_list("username", flat=True).distinct()
    blocked_user_list = ", ".join(blocked_usernames)
    message = f"Blocked Users: {blocked_user_list}"
    modeladmin.message_user(request, message)


show_blocked_users.short_description = "Show Blocked Users"


class AccessLogAdmin(admin.ModelAdmin):
    actions = [show_blocked_users]


admin.site.unregister(AccessLog)
admin.site.register(AccessLog, AccessLogAdmin)
