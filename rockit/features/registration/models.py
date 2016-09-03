from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from rockit.core.models import ModifiedModel


class Hello(ModifiedModel):
    """
    Track a hello requests
    """

    name = models.TextField(max_length=100, help_text=_("Name of requestee"))
    message = models.TextField(max_length=1000, help_text=_("Message of requestee"))
    identifier = models.UUIDField(primary_key=True, unique=True, editable=False, help_text=_("Identifier of requestee"))
