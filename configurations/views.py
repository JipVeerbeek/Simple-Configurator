from rest_framework import generics, views
from rest_framework.response import Response

from .models import Configuration, ConfigurationLine
from .serializers import ConfigurationLineSerializer, ConfigurationSerializer
from .services import PriceService


class ConfigurationCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationLineSerializer
    queryset = ConfigurationLine.objects.all()


class PriceListView(views.APIView):
    def get(self, request, configuration_id, *args, **kwargs):
        price_service = PriceService(configuration=configuration_id)
        price = price_service.calculate_order_price()
        return Response(price)
