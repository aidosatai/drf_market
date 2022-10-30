from rest_framework.routers import DefaultRouter

from account.views import CustonUserViewSet

router = DefaultRouter()
router.register('', CustonUserViewSet)

urlpatterns = [] + router.urls
