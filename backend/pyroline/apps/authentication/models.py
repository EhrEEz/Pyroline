import json
from django.contrib.admin.models import ACTION_FLAG_CHOICES
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import AccountManager
from shortuuid.django_fields import ShortUUIDField
from django.utils.translation import gettext, gettext_lazy as _
from simple_history.models import HistoricalRecords

STUDENT = 1
TEACHER = 2
ADMIN = 3
STAFF = 4

ROLE_CHOICES = [
    (STUDENT, "student"),
    (TEACHER, "teacher"),
    (ADMIN, "admin"),
    (STAFF, "staff"),
]

ADDITION = 1
CHANGE = 2
DELETION = 3

ACTION_FLAG_CHOICES = (
    (ADDITION, _('Addition')),
    (CHANGE, _('Change')),
    (DELETION, _('Deletion')),
)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = ShortUUIDField(
        length=8, max_length=40, prefix="u_", primary_key=True, unique=True
    )
    first_name = models.CharField("First Name", max_length=64)
    last_name = models.CharField("Last Name", max_length=64)
    username = models.CharField(
        "Username", max_length=64, null=False, blank=False, unique=True
    )
    email = models.EmailField(
        "Email Address", null=False, blank=False, unique=True)
    phone_number = models.CharField(
        "Phone Number", unique=True, max_length=10, blank=True, null=True
    )
    role = models.IntegerField(
        "Role", choices=ROLE_CHOICES, null=False, blank=False)
    date_joined = models.DateTimeField(
        "Date Joined",
        auto_now_add=True,
        editable=False,
    )
    is_active = models.BooleanField("Is active", default=True)
    is_staff = models.BooleanField("Is Staff", default=False)
    history = HistoricalRecords()
    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "role"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
