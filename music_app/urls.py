from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MusicApp')

urlpatterns = [
    re_path(r'^swagger/$', schema_view, name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('albums/', include('album.urls')),
]
