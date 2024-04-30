from configurations import views
from django.urls import path


urlpatterns = [
    path('', views.ConfigurationCreateView.as_view(), name='ConfigurationCreateView'),
]