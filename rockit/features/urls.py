import os

from django.conf.urls import include, url

from rockit import settings
from rockit.features import views

urlpatterns = [url(r'^$', views.FeaturesView.as_view(), name="features")]

for app in settings.INSTALLED_APPS:

    if app.startswith('%s' % 'rockit.features'):
        """
        Get all features defined in INSTALLED_APPS
        """

        entry = app.replace('.', '/')

        # If urls.py or urls directory exist then add it otherwise skip it
        if os.path.isfile('%s/urls.py' % entry) or os.path.isdir('%s/urls' % entry):
            urlpatterns.append(url(r'^%s/' % app.split('.')[-1], include('%s.urls' % app)))
