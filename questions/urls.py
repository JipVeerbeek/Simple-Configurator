from questions import views
from django.urls import path


urlpatterns = [
    path('', views.QuestionListView.as_view(), name='QuestionListView'),
]
