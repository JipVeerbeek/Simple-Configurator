from rest_framework import generics, views
from .models import Configuration, ConfigurationLine
from .serializers import ConfigurationSerializer, ConfigurationLineSerializer
from .services import PriceService


class ConfigurationCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationLineSerializer
    queryset = ConfigurationLine.objects.all()


class PriceListView(views.APIView):
    def get(self, request, configuration_id, *args, **kwargs):
        new_price = PriceService(configuration=configuration_id).calculateOrderPrice()
        return new_price
