from django.db import models


class Amenity(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE, related_name="amenities")
    name = models.CharField(max_length=48)

    class Meta:
        db_table = "amenity"
        unique_together = ("hotel", "name")

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
