from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

class Singer(models.Model):
    title = models.CharField(max_length=256, null=False, unique=True)
    created = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="updated", auto_now=True)

    class Meta:
        verbose_name = "Singer"
        verbose_name_plural = "Singers"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f'Singer {self.title}'
    
class Album(models.Model):
    title = models.CharField(max_length=256, null=False)
    singer = models.ForeignKey(Singer, null=False, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1500)])
    created = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="updated", auto_now=True)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f'Album {self.title}'


class Song(models.Model):
    title = models.CharField(max_length=256, null=False)
    albums = models.ManyToManyField(Album, through='SongAlbum')

    created = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="updated", auto_now=True)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f'Song {self.title}'

class SongAlbum(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name = "SongAlbum"
        verbose_name_plural = "SongAlbums"
        unique_together = (
            (
                "song",
                "album",
            ),
        )