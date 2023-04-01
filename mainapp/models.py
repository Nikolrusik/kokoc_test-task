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
    
    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"


class QuestionModel(models.Model):
    quest = models.TextField(verbose_name="Quest")
    survey = models.ForeignKey(
        SurveyModel,
        on_delete=models.CASCADE,
        verbose_name="Survey objects"
    )

    def __str__(self):
        return f"id: {self.id} | вопрос: {self.quest}"
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class AnswerModel(models.Model):
    answer = models.TextField(verbose_name="Answer")
    quest = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE,
        verbose_name="Quest object"
    )

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class CompletedSurveyModel(models.Model):
    survey = models.ForeignKey(
        SurveyModel,
        on_delete=models.CASCADE,
        verbose_name="Survey object"
    )
    user = models.ForeignKey(
        AbstractUserModel,
        on_delete=models.CASCADE,
        verbose_name="User"
    )
    status = models.CharField(
        verbose_name="Survey status",
        max_length=255,
        choices=CS_STATUSES,
        default="STARTED"
    )

    class Meta:
        verbose_name = "Completed survey"
        verbose_name_plural = "Completed surveys"


class ResultModel(models.Model):
    survey = models.ForeignKey(
        CompletedSurveyModel,
        on_delete=models.CASCADE,
        verbose_name="Survey object"
    )
    quest = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE,
        verbose_name="Quest object"
    )
    answer = models.ForeignKey(
        AnswerModel,
        on_delete=models.CASCADE,
        verbose_name="Answer object"
    )
    user = models.ForeignKey(
        AbstractUserModel,
        on_delete=models.CASCADE,
        verbose_name="User"
    )

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"