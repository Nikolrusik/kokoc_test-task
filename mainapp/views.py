from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models import F 
from mainapp import models as main_models
from authapp import models as auth_models

class MainPage(TemplateView):
    template_name = "mainapp/main.html"
    
    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['surveys'] = main_models.SurveyModel.objects.all()
        return context
    
class SurveyPage(TemplateView):
    template_name = "mainapp/pages/survey.html"
    
    def get_context_data(self, survey_id=None, quest_id=None, **kwargs):
        context = super(SurveyPage, self).get_context_data(**kwargs)
        context['quest'] = main_models.QuestionModel.objects.filter(survey__id=survey_id).first()
        if quest_id != 0:
            context['quest'] = main_models.QuestionModel.objects.filter(survey__id=survey_id, id=quest_id).first()
            context['next_quest'] = main_models.QuestionModel.objects.filter(survey__id=survey_id, id__gt=quest_id).first()
        else:
            context['next_quest'] = context['quest']
        context['answers'] = main_models.AnswerModel.objects.filter(quest_id=context['quest'].id)

        if self.request.GET.get('start'): # To avoid making a request every time
            if main_models.CompletedSurveyModel.objects.filter(survey__id=survey_id).exists() != True:
                new_completed = main_models.CompletedSurveyModel.objects.create(survey_id=survey_id, user=self.request.user, status='STARTED')
                new_completed.save()
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('answer'):
            survey_id = request.POST.get('survey_id')
            quest_id = request.POST.get('quest_id')
            answer_id = request.POST.get('answer')
            next_quest = request.POST.get('next_quest')
            completed_survey = main_models.CompletedSurveyModel.objects.get(survey__id=survey_id, user=request.user)
            if main_models.ResultModel.objects.filter(survey=completed_survey, quest__id=quest_id, user=request.user).exists():
                main_models.ResultModel.objects.filter(survey=completed_survey, quest__id=quest_id, user=request.user).update(answer_id=answer_id)
            else:
                new_result = main_models.ResultModel.objects.create(survey=completed_survey, quest_id=quest_id, user=request.user, answer_id=answer_id)
                new_result.save()
            if next_quest:
                return HttpResponseRedirect(f'/mainapp/survey/{survey_id}/{next_quest}/')
            else: 
                if main_models.CompletedSurveyModel.objects.filter(user=request.user, survey__id=survey_id, status="STARTED").exists():
                    request.user.balance = request.user.balance + main_models.SurveyModel.objects.get(id=survey_id).award
                    request.user.save()
                main_models.CompletedSurveyModel.objects.filter(user=request.user, survey__id=survey_id).update(status="COMPLETED")
                return HttpResponseRedirect(f'/mainapp/result/{survey_id}')


class ResultsPage(TemplateView):
    pass



