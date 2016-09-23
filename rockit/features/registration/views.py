from datetime import timedelta

from django.utils import timezone
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

        if not serializer.is_valid() and 'identifier' in serializer.errors:
            self.kwargs['pk'] = serializer.data['identifier']

            serializer = self.get_serializer(self.get_object())

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return super(HelloViewSet, self).create(request, args, kwargs)

    @detail_route(methods=['post'])
    def access(self, request, pk=None):

        hello = self.get_object()

        expired = timezone.now() + timedelta(minutes=2)

        if hello.is_blocked():
            d = {'status': 'BLOCKED'}
            s = status.HTTP_400_BAD_REQUEST
        elif hello.created < expired and hello.is_accepted():
            d = {'status': 'ACCEPT', 'token': '123' }
            s = status.HTTP_200_OK
        else:
            d = {'status': 'WAITING'}
            s = status.HTTP_200_OK

        return Response(d, status=s)

    @detail_route(methods=['post'])
    def accept(self, request, pk=None):
        """
        Accept specific hello request
        :param request:
        :param pk:
        :return:
        """
        self.get_object().accept()

        return Response({'status': 'accepted'}, status=status.HTTP_200_OK)
