from django.db import models


class PhoneColorChoice(models.TextChoices):
    WHITE = 'white', 'White'
    BLACK = 'black', 'Black'
    BLUE = 'blue', 'Blue'
    RED = 'red', 'Red'
    NO_COLOR = 'no_color', 'No Color'
