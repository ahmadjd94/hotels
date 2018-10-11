from datetime import datetime
from rest_framework.serializers import (
    ModelSerializer, CharField, IntegerField, ListField, PrimaryKeyRelatedField, FloatField,
    DateTimeField
)


from ..models import Hotel, Provider


class HotelsSerializer(ModelSerializer):
    name = CharField(required=True)
    provider = PrimaryKeyRelatedField(queryset=Provider.objects.all(), required=True)
    fare = FloatField(required=True, min_value=0)
    rate = IntegerField(required=True, min_value=0, max_value=5)
    city = CharField(min_length=3, max_length=3)

    availability = DateTimeField(default=datetime.now)

    class Meta:
        model = Hotel
        fields = ("availability", "name", "provider", "fare", "city", "rate")


class AvailableHotelsSerializer(ModelSerializer):
    hotel_name = CharField(read_only=True)
    fare = IntegerField(read_only=True)
    amenities = ListField()

    class Meta:
        model = Hotel
