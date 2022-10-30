from django.db.models import TextChoices


class CustomUserRoleChoice(TextChoices):
    SUPER_ADMIN = 'super_admin', 'СуперАдмин'
    ADMIN = 'admin', 'Админ'
    MANAGER = 'manager', 'Менеджер'
    DEFAULT = 'default', 'Обычный'

