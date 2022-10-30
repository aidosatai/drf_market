from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError

from utils.models import AbstarctUUID, AbstractTimeTracker
from utils.const import CustomUserRoleChoice
from account.managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin, AbstarctUUID, AbstractTimeTracker):
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Phone Number'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    iin = models.CharField(
        max_length=12,
        unique=True,
        verbose_name='IIN'
    )
    role = models.CharField(
        max_length=100,
        choices=CustomUserRoleChoice.choices,
        default=CustomUserRoleChoice.DEFAULT.value,
        verbose_name='Role'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name= 'is_active'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='is_staff'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='is_superuser'
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'iin']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-updated_at', '-created_at']

    # def clean(self):
    #     if self.is_staff and self.role != CustomUserRoleChoice.ADMIN.value or \
    #             (self.role == CustomUserRoleChoice.ADMIN.value and not self.is_staff):
    #         raise ValidationError('"role" or "is_staff" value is wrong!')
    #     return super(CustomUser, self.save(*args, **kwargs))


    def save(self, *args, **kwargs):
        # if self.is_staff and self.role != CustomUserRoleChoice.ADMIN.value or \
        #         (self.role == CustomUserRoleChoice.ADMIN.value and not self.is_staff):
        #     raise ValidationError('"role" or "is_staff" value is wrong!')

        if self.is_superuser:
            self.role = CustomUserRoleChoice.SUPER_ADMIN.value

        return super(CustomUser, self).save(*args, **kwargs)


