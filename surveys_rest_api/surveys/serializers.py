# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import (
    Answer, Option, Question, QuestionType, Section, Survey
)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'text')


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ('id', 'question_type', 'description')

        read_only_fields = ('id', 'question_type', 'description')


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id', 'text', 'hint',
            'required', 'question_type',
            'options',
        )


class SectionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Section
        fields = (
            'id', 'title', 'description', 'questions',
        )


class SurveySerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Survey
        fields = (
            'id', 'user', 'title', 'description', 'created_at',
            'updated_at', 'active', 'sections',
        )

        read_only_fields = ('created_at', 'updated_at', 'user')

    def create(self, validated_data):
        return create_survey(validated_data)


def create_options(options_data, question_created):
    for option in options_data:
        Option.objects.create(question=question_created, **option)


def create_questions(questions_data, section_created):
    for question in questions_data:
        options_data = question.pop('options')
        question_type = question.pop('question_type')
        question_created = Question.objects.create(
            section=section_created,
            question_type=question_type,
            **question
        )
        create_options(options_data, question_created)


def create_sections(sections_data, survey_created):
    for section in sections_data:
        questions_data = section.pop('questions')
        section_created = Section.objects.create(
            survey=survey_created,
            **section
        )
        create_questions(questions_data, section_created)


def create_survey(validated_data):
    sections_data = validated_data.pop('sections')
    survey_created = Survey.objects.create(**validated_data)
    create_sections(sections_data, survey_created)
    return survey_created
