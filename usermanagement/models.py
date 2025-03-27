from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL,
        null=True, blank=True
        )
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(
        max_length=255, null=True,
        blank=True
        )
    status = models.CharField(
        max_length=50, default='active'
        )
    phone_number = models.CharField(
        max_length=20, blank=True, null=True
        )
    address = models.TextField(
        blank=True, null=True
        )
    company_id = models.IntegerField(
        blank=True, null=True
        )
    otp = models.CharField(
        max_length=6, blank=True, null=True
        )
    otp_expired_at = models.DateTimeField(
        blank=True, null=True
        )

    def __str__(self):
        return self.username
