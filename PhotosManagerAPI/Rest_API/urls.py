from django.urls import path
from . import views

urlpatterns = [
    # /photos/api/
    path(
        route='api/',
        view=views.PhotoListCreateAPIView.as_view(),
        name='photo_rest_api'
    ),
    # /photos/api/:uuid/
    path(
        route='api/<uuid:uuid>/',
        view=views.PhotoRetrieveUpdateDestroyAPIView.as_view(),
        name='photo_rest_api'
    ),
    # /photos/api/import_from_json
    path(
        route='api/import_from_json/',
        view=views.PhotoImportAPIViewFromJson.as_view(),
        name='photo_rest_api_import_from_json'
    ),
    # /photos/api/import_from_url
    path(
        route='api/import_from_url/',
        view=views.PhotoImportAPIViewFromUrl.as_view(),
        name='photo_rest_api_import_from_url'
    )
]
