from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rockit.features.node import models
from rockit.features.node import serializers


class NodeView(APIView):
    """
    API collection of registration feature
    """

    def get(self, request):
        return Response({
            'node': reverse('node-list', request=request)
        })


class NodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = (IsAuthenticated,)

    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer
