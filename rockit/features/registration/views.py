import uuid

from django.core import exceptions
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if 'identifier' in serializer.data:
            try:
                self.kwargs['pk'] = serializer.data['identifier']

                hello = self.get_object()

                print hello

            except Http404:
                pass

        return super(HelloViewSet, self).create(request, args, kwargs)

    @detail_route(methods=['post'])
    def access(self, request, pk=None):
        return Response("test", status=status.HTTP_400_BAD_REQUEST)
