from rest_framework import generics
from .models import Configuration
from .serializers import ConfigurationSerializer

class ConfigurationCreateView(generics.CreateAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
