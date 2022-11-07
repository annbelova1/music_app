from rest_framework import status, viewsets
from rest_framework.response import Response

from album.models import Album, Song, Singer, SongAlbum
from .serializers import AlbumSerializer, SongSerializer, SingerSerializer, SongAlbumSerializer
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny


class AlbumApiView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class SongApiView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
      
class SingerApiView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongAlbumApiView(viewsets.ModelViewSet):
    queryset = SongAlbum.objects.all()
    serializer_class = SongAlbumSerializer
    