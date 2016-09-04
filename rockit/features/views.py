import os

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from rockit import settings


class FeaturesView(APIView):
    """
    All features found in application, read more in detail for each specific feature
    """

    def get(self, request):

        response = dict()

        for app in settings.INSTALLED_APPS:
            """
            Only looking for features namespace
            """
            if app.startswith('%s' % 'rockit.features'):

                entry = app.replace('.', '/')

                """
                If an urls file or directory exist then we should have a path to it
                """
                if os.path.isfile('%s/urls.py' % entry) or os.path.isdir('%s/urls' % entry):
                    app_name = app.split('.')[-1]

                    response.update({
                        app_name: reverse(app_name, request=request)
                    })

        return Response(response)