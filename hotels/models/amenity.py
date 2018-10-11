from django.db import models


class Amenity(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE, related_query_name="amenities")
    name = models.CharField(required=True, max_length=48)

    class Meta:
        db_table = "amenity"
