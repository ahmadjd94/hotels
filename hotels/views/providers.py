from ..models import Provider
from ..serializers import ProviderSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Providers(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        provider = Provider.objects.all()
        serializer = ProviderSerializer(provider, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)