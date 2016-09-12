from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class CreatedModel(models.Model):
    """
    Used to track creations of a model
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='system', max_length=70, help_text=_("Who created this model"))

    class Meta:
        abstract = True


class ModifiedModel(CreatedModel):
    """
    Used to track modification of a model
    """

    last_modified = models.DateTimeField(editable=False, default=timezone.now)
    last_modified_by = models.CharField(default='system', max_length=70, help_text=_("Who modified this model"))

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()

        super(ModifiedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

