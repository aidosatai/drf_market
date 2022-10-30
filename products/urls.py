from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import PhoneViewSet

router = DefaultRouter()

router.register('phones', PhoneViewSet)

urlpatterns = [] + router.urls
