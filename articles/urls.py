from articles import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='ArticleListView'),
]
