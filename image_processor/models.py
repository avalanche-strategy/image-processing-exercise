from django.db import models

class Image(models.Model):
    name = models.TextField()
    original_image_key = models.UUIDField()
    black_and_white_image_key = models.UUIDField(blank=True, null=True)
