from django.urls import include, path

from configurations import views

urlpatterns = [
    path(
        "",
        views.ConfigurationCreateView.as_view(),
        name="ConfigurationCreateView",
    ),
    path("answer/", views.AnswerCreateView.as_view(), name="AnswerCreateView"),
    path(
        "<configuration_id>/price/",
        views.PriceListView.as_view(),
        name="PriceListView",
    ),
    path("<configuration_id>/question/", include("questions.urls")),
    path(
        "<configuration_id>/question/<question_id>/article/",
        include("articles.urls"),
    ),
]
