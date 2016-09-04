from rest_framework import serializers

from rockit.features.registration.models import Hello


class HelloSerializer(serializers.ModelSerializer):
    """
    Hello serializer
    """

    class Meta:
        model = Hello
        fields = ('name', 'message', 'identifier', 'created')
        read_only_fields = ('created',)
