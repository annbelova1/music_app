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

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         self.permission_classes = [AllowAny, ]
    #     else:
    #         self.permission_classes = [IsAuthenticated, ]

    #     return super(AlbumApiView, self).get_permissions()



    # def create(self, request, *args, **kwargs):
    #     """
    #         Create a list of model instances if a list is provided or a
    #         single model instance otherwise.
    #     """
    #     try:
    #         data = request.data
    #         if isinstance(data, list):
    #             serializer = self.get_serializer(data=data, many=True)
    #         else:
    #             serializer = self.get_serializer(data=data)
    #         serializer.is_valid(raise_exception=True)

    #         serializer.save(user_id=self.request.user.id)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     except (TypeError, ValueError) as error:
    #         return Response({'error': f'{error.__class__.__name__}: {error}'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class SongApiView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    
class SingerApiView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongAlbumApiView(viewsets.ModelViewSet):
    queryset = SongAlbum.objects.all()
    serializer_class = SongAlbumSerializer