from collections import OrderedDict

from rest_framework.serializers import (
    CharField, IntegerField, Serializer, DateField, ValidationError
)


class CrazyHotelsQuerySerializer(Serializer):
    From = DateField(required=False)
    To = DateField(required=False)
    city = CharField(required=False)
    adultsCount = IntegerField(required=False)

    def to_internal_value(self, data):

        data = super(CrazyHotelsQuerySerializer, self).to_internal_value(data)

        if not (("From" in data and "To" in data) or
                ("From" not in data and "To" not in data)):
            missing = "To" if "From" in data else "From"
            errors = OrderedDict({
                missing: "can't search without %s field" % missing
            })

            raise ValidationError(errors)

        return data

    def to_representation(self, instance):
        data = super(CrazyHotelsQuerySerializer, self).to_representation(instance)
        kwargs = {}

        if "From" and "To" in data:
            kwargs.update({"availability__range": [data["From"], data["To"]]})

        if "city" in data:
            kwargs.update({
                "city": data["city"]
            })

        if "adultsCount" in data:
            kwargs.update({
                "adultsCount": data["adultsCount"]
            })

        return kwargs


