from rest_framework import serializers

from rockit.features.registration.models import Member


class HelloSerializer(serializers.ModelSerializer):
    """
    Hello serializer
    """

    access = serializers.HyperlinkedIdentityField(
        view_name='hello-access',
        lookup_field='identifier',
        lookup_url_kwarg='pk'
    )

    class Meta:
        model = Member
        fields = ('access', 'name', 'message', 'identifier', 'created')
        read_only_fields = ('created',)


class HelloAccessSerializer(serializers.ModelSerializer):
    """
    Serializer for giving access to hello
    """

    class Meta:
        model = Member
        fields = ('created',)

    def validate_created(self, value):
        raise serializers.ValidationError("Blog post is not about Django")

        return value
