from ..models import Amenity, Hotel
from ..serializers import AmenitySerializer


from rest_framework.views import APIView
from rest_framework.response import Response


class HotelAmenity(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, hotel_id, format=None):
        hotel = Hotel.objects.get(id=hotel_id)
        serializer = AmenitySerializer(hotel.amenities, many=True)

        return Response(serializer.data)

    def post(self, request, hotel_id, format=None):
        hotel = Hotel.objects.get(id=hotel_id)
        serializer = AmenitySerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            data.update({
                "hotel": hotel
            })
            amenity = Amenity(**data)
            amenity.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
