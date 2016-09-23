from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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


class UserProfile(ModifiedModel):
    """
    Create a customized profile that integrates with django user
    """

    user = models.OneToOneField(User, related_name='profile', editable=False)
    name = models.TextField(max_length=100, help_text=_("Name of the plugin"))
    uuid = models.TextField(editable=False, help_text=_("Unique identifier of user"))


@receiver(post_save, sender=User, dispatch_uid="user-create-profile")
def create_user_profile(sender, instance, created, **kwargs):
    """
    Callback for creating a partner if user profile is created
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        UserProfile.objects.create(user=instance, uuid=instance.username)
