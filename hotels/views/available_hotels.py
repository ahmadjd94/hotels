from ..models import Hotel
from ..serializers import AvailableHotelsSerializer, HotelsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AvailableHotels(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializer = AvailableHotelsSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HotelsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)