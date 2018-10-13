from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Hotel
from ..serializers import AvailableHotelsSerializer, HotelsSerializer
from ..query import AvailableHotelsQuerySerializer


class AvailableHotel(APIView):
    """
    AvailableHotel Api
    """
    def get(self, request):
        query = AvailableHotelsQuerySerializer(data=request.query_params)

        if query.is_valid():
            hotels = Hotel.objects.filter(**query.data)
            serializer = AvailableHotelsSerializer(hotels, many=True)
            return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=query.errors)
