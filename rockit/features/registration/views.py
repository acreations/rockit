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
        return Response("test", status=status.HTTP_400_BAD_REQUEST)
