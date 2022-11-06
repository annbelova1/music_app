from django.contrib import admin
from album.models import Album, Singer,  Song
# Register your models here.

admin.site.register(Album)
admin.site.register(Singer)
admin.site.register(Song)
