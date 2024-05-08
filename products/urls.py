from products import views
from django.urls import path, include


urlpatterns = [
    path('', views.ProductListView.as_view(), name='ProductListView'),
    path('<product_id>/question/', include('questions.urls')),
]
