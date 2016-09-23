from rest_framework import serializers

from rockit.features.registration.models import Mingle


class HelloSerializer(serializers.ModelSerializer):
    """
    Serialize a hello request
    """

    access = serializers.HyperlinkedIdentityField(
        view_name='hello-access',
        lookup_field='identifier',
        lookup_url_kwarg='pk'
    )

    class Meta:
        model = Mingle
        fields = ('access', 'name', 'message', 'identifier', 'created')
        read_only_fields = ('created',)
