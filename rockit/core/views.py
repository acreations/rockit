from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class RockitView(APIView):
    """
    Rock it at home with automation
    """

    def get_view_name(self):
        return "Rockit"

    def get(self, request):
        return Response({
            'features': reverse('features', request=request),
        })
