from django.urls import path
from rest_framework.routers import SimpleRouter

from musics.views import CDViewSet

router = SimpleRouter()
router.register('', CDViewSet, basename="musics")

urlpatterns = router.urls
