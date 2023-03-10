from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig


app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPage.as_view(), name="main"),
    path("survey/<int:survey_id>/<int:quest_id>/", views.SurveyPage.as_view(), name="survey"),
    path("result/<int:id>/", views.ResultsPage.as_view(), name='result'),
    path("all_results/", views.AllResultsPage.as_view(), name="all_results")
]