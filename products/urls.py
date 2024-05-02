from products import views
from django.urls import path


urlpatterns = [
    path('', views.ProductListView.as_view(), name='ProductListView'),
]
