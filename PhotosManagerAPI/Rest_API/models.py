from django.db import models
import uuid as uuid_lib
from io import BytesIO
import requests
from PIL import Image


class Photo(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    title = models.CharField(max_length=200)
    albumId = models.PositiveIntegerField(blank=False, null=False)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    dominant_color = models.CharField(max_length=6)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def _get_image_size(self):
        expanded_url = str(self.url) + ".png"
        response = requests.get(expanded_url)
        return Image.open(BytesIO(response.content)).size

    def _get_dominant_color(self):
        expanded_url = str(self.url) + ".png"
        image = requests.get(expanded_url)
        original_image = Image.open(BytesIO(image.content))
        color_palette = original_image.getpalette()  # get palette as [r,g,b,r,g,b,...]
        color_palette = [color_palette[3 * n:3 * n + 3] for n in
                         range(len(color_palette))]  # group 3 by 3 = [[r,g,b],[r,g,b],...]
        color_count = sorted([(n, color_palette[m]) for n, m in
                              original_image.getcolors()], reverse=True)  # assign pixel quantity to each RGB color
        dominant_color = color_count[0]  # Quantity of pixels of dominant color (as RGB)

        dominant_hex_color = '%02x%02x%02x' % (dominant_color[1][0], dominant_color[1][1], dominant_color[1][2])
        return dominant_hex_color

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.width, self.height = self._get_image_size()
        self.dominant_color = self._get_dominant_color()
        super().save()
