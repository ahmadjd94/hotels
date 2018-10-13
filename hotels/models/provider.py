from django.db import models


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=48)

    objects = models.Manager()

    class Meta:
            db_table = "provider"

    def __str__(self):
        return self.name
