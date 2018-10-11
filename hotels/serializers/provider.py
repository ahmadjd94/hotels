from rest_framework.serializers import ModelSerializer, CharField

from ..models import Provider


class ProviderSerializer(ModelSerializer):
	name = CharField()

	class Meta:
		model = Provider
		fields = ("name",)
