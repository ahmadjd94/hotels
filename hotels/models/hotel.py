from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE, related_query_name="hotels")
    name = models.CharField(blank=False, max_length=48)
    availability = models.DateTimeField(blank=False)
    city = models.CharField(max_length=2, blank=False)
    fare = models.SmallIntegerField()
    rate = models.SmallIntegerField()
    number_of_adults = models.SmallIntegerField()

    objects = models.Manager()

    class Meta:
        db_table = "hotel"
