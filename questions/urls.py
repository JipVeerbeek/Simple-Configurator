from django.urls import path

from questions import views

urlpatterns = [
    path("", views.QuestionListView.as_view(), name="QuestionListView"),
]
