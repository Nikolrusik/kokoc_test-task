from django.contrib import admin
from mainapp import models


@admin.register(models.SurveyModel)
class SurveyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'award']

@admin.register(models.AnswerModel)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'quest', 'answer']

@admin.register(models.QuestionModel)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey', 'quest']

@admin.register(models.CompletedSurveyModel)
class CompletedSurveyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey', 'user', 'status']


@admin.register(models.ResultModel)
class ResultModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey', 'quest', 'answer', 'user']