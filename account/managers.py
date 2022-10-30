from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, phone, password, **extra_fields):

        if not phone or phone is None:
            raise ValueError('User MUST have Phone number!')

        user_instance = self.model(
            phone=phone,
            **extra_fields
        )

        if password:
            user_instance.set_password(password)
        user_instance.save()

        return user_instance

    def create_user(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phone, password, **extra_fields)
