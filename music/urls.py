from .views import SongViewSet, AlbumViewSet, ArtistViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', SongViewSet)
router.register('albums', AlbumViewSet)
router.register('artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls))
]