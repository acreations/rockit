from django.conf.urls import include, url
from rest_framework import routers

from rockit.core import views

router = routers.SimpleRouter()

urlpatterns = router.urls
urlpatterns.append(url(r'^$', views.RockitView.as_view(), name="root"))
urlpatterns.append(url(r'^features/', include('rockit.features.urls')))
