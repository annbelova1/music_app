from rest_framework import serializers
from .models import Album, Singer, Song, SongAlbum

class SingerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Singer
        fields = ("id", "title")
 
class AlbumSerializer(serializers.ModelSerializer):
    singer = SingerSerializer

    class Meta:
        model = Album
        fields = ("id", "title", "singer", "year")
               
class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer
    # user_id = serializers.ReadOnlyField()
    # fuel_consumption_per_minute = serializers.SerializerMethodField(
    #     source='get_fuel_consumption_per_minute'
    # )

    class Meta:
        model = Song
        fields = ("id", "title", "albums")
        

class SongAlbumSerializer(serializers.ModelSerializer):
    album = AlbumSerializer
    song = SongSerializer
    # user_id = serializers.ReadOnlyField()
    # fuel_consumption_per_minute = serializers.SerializerMethodField(
    #     source='get_fuel_consumption_per_minute'
    # )

    class Meta:
        model = SongAlbum
        fields = ("id", "song", "album", "number")     
        unique_together = (
            (
                "song",
                "album",
            ),
        )




