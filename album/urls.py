from django.conf.urls import url
from django.urls import include

from rest_framework import routers
from album.views import AlbumApiView, SongApiView, SingerApiView, SongAlbumApiView

router = routers.DefaultRouter()
router.register(r'albums', AlbumApiView, basename='albums')
router.register(r'songs', SongApiView, basename='songs')
router.register(r'singers', SingerApiView, basename='singers')
router.register(r'song_to_albums', SongAlbumApiView, basename='add_song_to_album')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
