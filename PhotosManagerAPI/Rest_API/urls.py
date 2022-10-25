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
    )
]
