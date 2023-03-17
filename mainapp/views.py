from typing import Dict, Any
from django.http import HttpResponseRedirect, HttpRequest
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from mainapp import models as main_models
from shopapp.views import LoginUrlUpdate


class MainPage(LoginUrlUpdate, TemplateView):
    template_name: str = "mainapp/main.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(MainPage, self).get_context_data(**kwargs)
        context['surveys'] = main_models.SurveyModel.objects.all()
        return context


class SurveyPage(LoginUrlUpdate, TemplateView):
    template_name: str = "mainapp/pages/survey.html"

    def get_context_data(self, survey_id: int = None, quest_id: int = None, **kwargs: Any) -> Dict[str, Any]:
        context = super(SurveyPage, self).get_context_data(**kwargs)
        context['quest'] = main_models.QuestionModel.objects.filter(
            survey__id=survey_id).first()
        if quest_id != 0:
            context['quest'] = main_models.QuestionModel.objects.filter(
                survey__id=survey_id, id=quest_id).first()
            context['next_quest'] = main_models.QuestionModel.objects.filter(
                survey__id=survey_id, id__gt=quest_id).first()
        else:
            context['next_quest'] = context['quest']
        context['answers'] = main_models.AnswerModel.objects.filter(
            quest_id=context['quest'].id)

        if self.request.GET.get('start'):  # To avoid making a request every time
            if main_models.CompletedSurveyModel.objects.filter(survey__id=survey_id).exists() != True:
                new_completed = main_models.CompletedSurveyModel.objects.create(
                    survey_id=survey_id, user=self.request.user, status='STARTED')
                new_completed.save()
        return context

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        if request.POST.get('answer'):
            survey_id: int = int(request.POST.get('survey_id'))
            quest_id: int = int(request.POST.get('quest_id'))
            answer_id: int = int(request.POST.get('answer'))
            next_quest: int = int(request.POST.get('next_quest'))
            completed_survey: main_models.CompletedSurveyModel = main_models.CompletedSurveyModel.objects.get(
                survey__id=survey_id, user=request.user)
            if main_models.ResultModel.objects.filter(survey=completed_survey, quest__id=quest_id, user=request.user).exists():
                main_models.ResultModel.objects.filter(
                    survey=completed_survey, quest__id=quest_id, user=request.user).update(answer_id=answer_id)
            else:
                new_result: main_models.ResultModel = main_models.ResultModel.objects.create(
                    survey=completed_survey, quest_id=quest_id, user=request.user, answer_id=answer_id)
                new_result.save()
            if next_quest:
                return HttpResponseRedirect(f'/mainapp/survey/{survey_id}/{next_quest}/')
            else:
                if main_models.CompletedSurveyModel.objects.filter(user=request.user, survey__id=survey_id, status="STARTED").exists():
                    request.user.balance = request.user.balance + \
                        main_models.SurveyModel.objects.get(id=survey_id).award
                    request.user.save()
                main_models.CompletedSurveyModel.objects.filter(
                    user=request.user, survey__id=survey_id).update(status="COMPLETED")
                return HttpResponseRedirect(f'/mainapp/result/{completed_survey.id}')


class ResultsPage(LoginUrlUpdate, TemplateView):
    template_name: str = "mainapp/pages/results.html"

    def get_context_data(self, id: int = None, **kwargs: Any) -> Dict[str, Any]:
        context = super(ResultsPage, self).get_context_data(**kwargs)
        context['survey'] = main_models.CompletedSurveyModel.objects.get(id=id)
        context['result'] = main_models.ResultModel.objects.filter(
            survey__id=id, user=self.request.user)
        return context


class AllResultsPage(LoginUrlUpdate, TemplateView):
    template_name: str = "mainapp/pages/all_results.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(AllResultsPage, self).get_context_data(**kwargs)
        context['results'] = main_models.CompletedSurveyModel.objects.filter(
            user=self.request.user)
        return context
