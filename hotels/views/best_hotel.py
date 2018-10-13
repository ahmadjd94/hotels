from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Hotel
from ..serializers import BestHotelsSerializer
from ..query import AvailableHotelsQuerySerializer


class BestHotel(APIView):
    """
    Best Hotel API
    """
    def get(self, request, format=None):
        query = AvailableHotelsQuerySerializer(data=request.query_params)

        if query.is_valid():
            hotels = Hotel.objects.filter(**query.data)
            serializer = BestHotelsSerializer(hotels, many=True)
            return Response(serializer.data)

        return Response(status=400, data=query.errors)
