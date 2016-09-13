from rest_framework import serializers

from rockit.features.registration.models import Member


class HelloSerializer(serializers.ModelSerializer):
    """
    Hello serializer
    """

    class Meta:
        model = Member
        fields = ('name', 'message', 'identifier', 'created')
        read_only_fields = ('created',)
