from django.conf.urls import url
from rest_framework import routers

from rockit.features.node import views

router = routers.SimpleRouter()
router.register('node', views.NodeViewSet, 'node')

urlpatterns = router.urls
urlpatterns.append(url(r'^$', views.NodeView.as_view(), name="node"))
