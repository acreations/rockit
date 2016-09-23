from rest_framework import serializers
from rockit.features.node.models import Node


class NodeSerializer(serializers.ModelSerializer):
    """
    Serialize a node
    """

    class Meta:
        model = Node
        fields = ('uuid', 'name', 'description', 'belongs_to', 'created')
        read_only_fields = ('created',)
