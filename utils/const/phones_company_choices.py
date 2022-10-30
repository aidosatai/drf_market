from django.db import models


class PhoneCompanyChoice(models.TextChoices):
    APPLE = 'apple', 'Apple'
    SAMSUNG = 'samsung', 'Samsung'
    XIAOMI = 'xiaomi', 'Xiaomi'
    BLACKBERRY = 'blackberry', 'BlackBerry'
    OTHER = 'other', 'Other'
