from rest_framework.serializers import (
    ModelSerializer, CharField
)

from ..models import Amenity


class AmenitySerializer(ModelSerializer):
    name = CharField()

    class Meta:
        model = Amenity
        fields = ("name",)
