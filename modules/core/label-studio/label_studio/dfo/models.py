from django.db import models

class ZoomData(models.Model):
    zoom_position_x = models.FloatField()
    zoom_position_y = models.FloatField()
    zoom_scale = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)