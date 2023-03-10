from django.db import models
from authapp.models import AbstractUserModel


CS_STATUSES = (
    ("COMPLETED", "Completed"),
    ("STARTED", "Started")
)

class SurveyModel(models.Model):
    name = models.CharField(verbose_name="Survey name", max_length=255)
    description = models.TextField(
        verbose_name="Question description",
        blank=True,
        null=True
    )
    award = models.FloatField(
        verbose_name="Question award",
        default=0.0
    )
    def __str__(self):
        return f"id: {self.id} | Опрос: {self.name}"

class QuestionModel(models.Model):
    quest = models.TextField(verbose_name="Quest")
    survey = models.ForeignKey(SurveyModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"id: {self.id} | вопрос: {self.quest}"

class AnswerModel(models.Model):
    answer = models.TextField(verbose_name="Answer")
    quest = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)


class CompletedSurveyModel(models.Model):
    survey = models.ForeignKey(SurveyModel, on_delete=models.CASCADE)
    user = models.ForeignKey(AbstractUserModel, on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name="Survey status",
        max_length=255,
        choices=CS_STATUSES,
        default="STARTED"
    )

class ResultModel(models.Model):
    survey = models.ForeignKey(CompletedSurveyModel, on_delete=models.CASCADE)
    quest = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerModel, on_delete=models.CASCADE)
    user = models.ForeignKey(AbstractUserModel, on_delete=models.CASCADE)


