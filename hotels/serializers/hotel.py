from datetime import datetime,date
from rest_framework.serializers import (
    ModelSerializer, CharField, IntegerField, PrimaryKeyRelatedField, FloatField,
    DateField
)

from .amenity import AmenitySerializer
from ..models import Hotel, Provider


class HotelsSerializer(ModelSerializer):
    name = CharField(required=True)
    provider = PrimaryKeyRelatedField(queryset=Provider.objects.all(), required=True)
    fare = FloatField(required=True, min_value=0)
    rate = IntegerField(required=True, min_value=0, max_value=5)
    number_of_adults = IntegerField(required=True, min_value=0, max_value=20)
    discount = FloatField(required=False, min_value=0, max_value=1, default=0)
    city = CharField(min_length=3, max_length=3)
    availability = DateField(default=date.today)

    class Meta:
        model = Hotel
        fields = ("availability", "name", "provider", "fare", "city", "rate",
                  "number_of_adults", "discount")


class AvailableHotelsSerializer(ModelSerializer):
    hotelName = CharField(read_only=True)
    provider = CharField(read_only=True)
    fare = IntegerField(read_only=True)
    number_of_adults = IntegerField(required=True)

    class Meta:
        model = Hotel
        fields = ("hotelName", "provider", "availability", "fare", "number_of_adults")


class BestHotelsSerializer(ModelSerializer):
    hotel = CharField(read_only=True,source="name")
    hotelRate = IntegerField(read_only=True, source="rate")
    hotelFare = IntegerField(read_only=True, source="fare")

    roomAmenities = AmenitySerializer(many=True, source="amenities")

    class Meta:
        model = Hotel
        fields = ("hotel", "hotelRate", "hotelFare", "roomAmenities")

    def to_representation(self, instance):
        data = super(BestHotelsSerializer, self).to_representation(instance)
        data["roomAmenities"] = ",".join([amenity["name"] for amenity in data["roomAmenities"]])

        return data


class CrazyHotelsSerializer(ModelSerializer):
    hotelName = CharField(read_only=True, source="name")
    rate = IntegerField(read_only=True)
    price = IntegerField(read_only=True, source="fare")
    adultsCount = IntegerField(read_only=True, source="number_of_adults")
    discount = FloatField(read_only=True)
    amenities = AmenitySerializer(many=True)

    class Meta:
        model = Hotel
        fields = ("hotelName", "rate", "price", "discount", "amenities", "adultsCount")

    def to_representation(self, instance):
        data = super(CrazyHotelsSerializer, self).to_representation(instance)
        data["rate"] = "*" * data["rate"]
        data["amenities"] = [amenity["name"] for amenity in data["amenities"]]

        return data
