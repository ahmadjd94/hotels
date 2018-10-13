from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from ..models import Provider
from ..serializers import HotelsSerializer


class HotelView(APIView):

	def post(self, request, provider_id):
		"""
		Use this view to create hotels belonging to a provider
		:param request: HTTP Request
		:param provider_id: Provider primary Key
		:return: Response
		"""
		provider = get_object_or_404(Provider, id=provider_id)
		data = request.data
		data.update({
			"provider": provider.id
		})
		serializer = HotelsSerializer(data=data)
		if serializer.is_valid():

			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)