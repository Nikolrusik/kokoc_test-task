from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig


app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPage.as_view(), name="main"),
    path("survey/<int:survey_id>/<int:quest_id>/", views.SurveyPage.as_view(), name="survey"),
]