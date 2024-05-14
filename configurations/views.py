from rest_framework import generics
from .models import Configuration
from .serializers import ConfigurationSerializer, ConfigurationLineSerializer, PriceSerializer
from .services import PriceService


class ConfigurationCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationLineSerializer
    queryset = Configuration.objects.all()


class PriceListView(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        configuration_id = self.kwargs.get('configuration_id')

        new_price = PriceService(configuration=configuration_id).calculateOrderPrice()

        return {'price': new_price}
