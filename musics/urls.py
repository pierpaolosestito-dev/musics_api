from django.urls import path
from rest_framework.routers import SimpleRouter

from musics.views import CDViewSet, CDByArtist, CDByName, CDByPublishedBy

router = SimpleRouter()
router.register('', CDViewSet, basename="musics")

urlpatterns = [
    path('byartist', CDByArtist.as_view()),
    path('byname', CDByName.as_view()),
    path('by_published_by', CDByPublishedBy.as_view())
]
urlpatterns += router.urls
