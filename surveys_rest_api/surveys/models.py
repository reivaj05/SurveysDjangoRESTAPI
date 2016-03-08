from __future__ import unicode_literals

from django.db import models
from accounts.models import UserProfile


# Create your models here.
class Survey(models.Model):

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"

    title = models.CharField(max_length=80)
    description = models.TextField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(UserProfile, related_name='surveys')

    def __str__(self):
        return self.title


class Section(models.Model):

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    title = models.CharField(max_length=80)
    description = models.TextField(blank=True, max_length=200)
    survey = models.ForeignKey(Survey)

    def __str__(self):
        return self.title


class QuestionType(models.Model):

    class Meta:
        verbose_name = "QuestionType"
        verbose_name_plural = "QuestionTypes"

    question_type = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.type + ': ' + self.description


class Question(models.Model):

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    text = models.CharField(max_length=80)
    hint = models.CharField(blank=True, max_length=80)
    required = models.BooleanField(default=False)
    question_type = models.ForeignKey(QuestionType)
    section = models.ForeignKey(Section)

    def __str__(self):
        self.text


class Option(models.Model):

    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"

    text = models.CharField(max_length=80)
    question = models.ForeignKey(Question)

    def __str__(self):
        self.text


class Answer(models.Model):

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    text = models.CharField(max_length=80)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.text
