from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(
        max_length=255,
        unique=True,
        validators=[username_validator],
        help_text=_(
            "Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only"
        ),
        error_messages={"unique": _("A user with that username already exists")},
    )

    def __str__(self):
        return self.username
