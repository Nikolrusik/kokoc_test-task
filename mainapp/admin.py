from django.contrib import admin
from mainapp import models


class QuestsInline(admin.StackedInline):
    model = models.QuestionModel
    extra = 5

class AnswerInline(admin.StackedInline):
    model = models.AnswerModel
    extra = 4

@admin.register(models.QuestionModel)
class QuestionModelAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    list_display = ['id', 'survey', 'quest']


@admin.register(models.SurveyModel)
class SurveyModelAdmin(admin.ModelAdmin):
    inlines = [QuestsInline]
    list_display = ['id', 'name', 'description', 'award']