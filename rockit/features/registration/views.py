from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rockit.features.registration import models
from rockit.features.registration import serializers


class RegistrationView(APIView):
    """
    API collection of registration feature
    """

    def get(self, request):
        return Response({
            'hello': reverse('hello-list', request=request),
        })


class HelloViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = models.Member.objects.all()
    serializer_class = serializers.HelloSerializer
