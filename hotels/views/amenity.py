from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import Amenity, Hotel
from ..serializers import AmenitySerializer




class HotelAmenity(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, hotel_id, format=None):
        """
        Use this view to get amenities of a certain Hotel
        :param request:
        :param hotel_id:
        :param format:
        :return:
        """
        hotel = get_object_or_404(Hotel, id=hotel_id)

        serializer = AmenitySerializer(hotel.amenities, many=True)

        return Response(serializer.data)

    def post(self, request, hotel_id, format=None):
        """
        Use this view to create Amenities belonging to a Hotel
        :param request:
        :param hotel_id:
        :param format:
        :return:
        """
        hotel = get_object_or_404(Hotel, id=hotel_id)

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
