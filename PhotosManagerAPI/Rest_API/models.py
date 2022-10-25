from django.db import models
import uuid as uuid_lib


class Photo(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    title = models.CharField(max_length=200)
    albumID = models.PositiveIntegerField()
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    dominant_color = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.title
