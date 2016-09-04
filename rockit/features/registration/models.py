from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from rockit.core.models import ModifiedModel


class Hello(ModifiedModel):
    """
    Track a hello requests
    """

    name = models.TextField(max_length=100, help_text=_("Please specify a name"))
    message = models.TextField(max_length=1000, help_text=_("Any hello message?"))
    identifier = models.UUIDField(primary_key=True, unique=True, help_text=_("Unique identifier (uuid4)"))