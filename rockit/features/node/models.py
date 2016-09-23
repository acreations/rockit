from django.db import models
from django.utils.translation import ugettext as _
from rockit.core.models import ModifiedModel, UserProfile


class Node(ModifiedModel):
    """
    Track a hello requests
    """
    uuid = models.CharField(max_length=36, unique=True, editable=False, help_text=_("Unique identifier"))
    name = models.CharField(max_length=200, default='undefined', help_text=_("Name of this node"))
    belongs_to = models.ForeignKey(UserProfile)
    description = models.CharField(max_length=500, blank=True, help_text=_("Descriptive information"))
