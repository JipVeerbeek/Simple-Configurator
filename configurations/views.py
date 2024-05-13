from rest_framework import generics
from .models import Configuration
from .serializers import ConfigurationSerializer, ConfigurationLineSerializer
from .services import PriceService


class ConfigurationCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = ConfigurationLineSerializer
    queryset = Configuration.objects.all()

    def perform_create(self, serializer):
        created_answer = serializer.save()
        new_price = PriceService(configuration=created_answer.configuration_id).calculateOrderPrice()

        return new_price
