from collections import OrderedDict
from datetime import datetime
from rest_framework.serializers import (
    ModelSerializer, CharField, IntegerField, PrimaryKeyRelatedField, FloatField,
    DateTimeField,Serializer, DateField, ValidationError
)


from ..models import Hotel, Provider


class HotelsSerializer(ModelSerializer):
    name = CharField(required=True)
    provider = PrimaryKeyRelatedField(queryset=Provider.objects.all(), required=True)
    fare = FloatField(required=True, min_value=0)
    rate = IntegerField(required=True, min_value=0, max_value=5)
    number_of_adults = IntegerField(required=True, min_value=0, max_value=20)
    city = CharField(min_length=3, max_length=3)
    availability = DateTimeField(default=datetime.now)

    class Meta:
        model = Hotel
        fields = ("availability", "name", "provider", "fare", "city", "rate", "number_of_adults")


class AvailableHotelsQuerySerializer(Serializer):
    fromDate = DateField(required=False)
    toDate = DateField(required=False)
    city = CharField(required=False)
    numberOfAdults = IntegerField(required=False)

    def to_internal_value(self, data):

        data = super(AvailableHotelsQuerySerializer, self).to_internal_value(data)

        if not (("fromDate" in data and "toDate" in data) or
                ("fromDate" not in data and "toDate" not in data)):
            missing = "toDate" if "fromDate" in data else "fromDate"
            errors = OrderedDict({
                missing: "can't search without %s field" % missing
            })

            raise ValidationError(errors)

        return data

    def to_representation(self, instance):
        data = super(AvailableHotelsQuerySerializer, self).to_representation(instance)
        kwargs = {}

        if "fromDate" and "toDate" in data:
            kwargs.update({"availability__range": [data["fromDate"], data["toDate"]]})

        if "city" in data:
            kwargs.update({
                "city": data["city"]
            })

        if "numberOfAdults" in data:
            kwargs.update({
                "number_of_adults": data["numberOfAdults"]
            })

        return kwargs
    

