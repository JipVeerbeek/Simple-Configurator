from rest_framework import generics, views
from rest_framework.response import Response
from django.utils.module_loading import import_string
from django.conf import settings

from .models import Configuration, ConfigurationLine
from .serializers import ConfigurationLineSerializer, ConfigurationSerializer


class ConfigurationCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationLineSerializer
    queryset = ConfigurationLine.objects.all()


class PriceListView(views.APIView):
    def get(self, request, configuration_id, *args, **kwargs):
        PriceService = self.get_price_service()(configuration_id=configuration_id)
        price = PriceService.calculate_order_price()
        return Response(price)

    def get_price_service(self):
        price_service_path = settings.PRICE_SERVICE
        PriceServiceClass = import_string(price_service_path)
        return PriceServiceClass
