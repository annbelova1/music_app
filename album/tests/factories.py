import factory
from album.models import Singer, Song, Album
@factory.Faker.override_default_locale('en_US')

class SingerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Singer

    title = factory.Faker("title")
    created = factory.Faker("date_time")

class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Song

    title = factory.Faker("title")
    created = factory.Faker("date_time")
    
class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    title = factory.Faker("title")
    singer = factory.SubFactory(SingerFactory)
    year = factory.Sequence(lambda n: f"year {n}")
    created = factory.Faker("date_time")
