from django.contrib.auth.models import User


def create_user(uuid, name):
    """
    Create a user with username as uuid
    :param uuid:
    :param name:
    :param password:
    :return:
    """

    try:
        user = User.objects.get(username=uuid)
    except User.DoesNotExist:
        user = User.objects.create_user(uuid)
        user.profile.name = name
        user.profile.save()

    return user
