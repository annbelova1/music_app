from django.conf import settings
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from album.models import Song, Singer, Album, SongAlbum
from album.tests.factories import SingerFactory, SongFactory, AlbumFactory


class AlbumAPITestCase(APITestCase):

    def setUp(self):
        self.song: Song = SongFactory()
        self.singer: Singer = SingerFactory()
        self.album: Singer = AlbumFactory()
        self.request_data = {'song': self.song, 'album': self.album, 'number': 1}

    def _subject(self, data={}):
        modified_url = reverse('song_to_albums-list')
        return self.client.post(modified_url, data, format='json')

    def test_add_song_to_album_success(self):
        response = self._subject(data=self.request_data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SongAlbum.objects.count(), 1)
        print(response.json())

    # def test_create_airplane_more_than_allowed(self):
    #     """
    #     Try to create more planes for user than AIRPLANES_LIMIT
    #     raise ValueError
    #     """
    #     response = self._subject(data=self.over_limit_request_data)
    #     expected_error = {
    #         'error': f'ValueError: You can create only {settings.AIRPLANES_LIMIT} planes'
    #     }

    #     self.assertEqual(AlbumSong.objects.count(), 0)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertDictEqual(response.data, expected_error)
    
