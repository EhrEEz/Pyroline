from __future__ import unicode_literals
from simple_history.admin import SimpleHistoryAdmin

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin, SimpleHistoryAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "user_id",
        "username",
        "first_name",
        "last_name",
    )
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("role", "is_staff", "is_active")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("user_id", "username", "first_name")
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

# @admin.register(User)
# class CustomUserAdmin(admin.ModelAdmin):
#     pass
#     list_display = [
#         "user_id",
#         "phone_number",
#         "first_name",
#         "last_name",
#         "role",
#         "dob",
#     ]

#     class Meta:
#         model = User
