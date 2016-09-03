from django.conf.urls import include, url
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = router.urls
urlpatterns.append(url(r'^features/', include('rockit.features.urls')))
