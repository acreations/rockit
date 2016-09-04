from django.conf.urls import url
from rest_framework import routers

from rockit.features.registration import views

router = routers.SimpleRouter()
router.register('hello', views.HelloViewSet, 'hello')

urlpatterns = router.urls
urlpatterns.append(url(r'^$', views.RegistrationView.as_view(), name="registration"))
