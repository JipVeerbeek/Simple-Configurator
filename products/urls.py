from products import views
from django.urls import path


urlpatterns = [
    path('product/', views.ProductListView.as_view(), name='ProductListView'),
]