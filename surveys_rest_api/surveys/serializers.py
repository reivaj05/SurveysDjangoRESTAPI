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
        sections_data = validated_data.pop('sections')
        survey_created = Survey.objects.create(**validated_data)
        for section in sections_data:
            questions_data = section.pop('questions')
            section_created = Section.objects.create(
                survey=survey_created,
                **section
            )
            for question in questions_data:
                options_data = question.pop('options')
                question_type = question.pop('question_type')
                question_created = Question.objects.create(
                    section=section_created,
                    question_type=question_type,
                    **question
                )
                for option in options_data:
                    Option.objects.create(question=question_created, **option)

        # self.create_data(sections_data, Section, 'survey=fk', survey)
        return survey_created

    def create_data(self, data, model, assignment, fk):
        print eval(assignment)
        for element in data:
            model.objects.create(eval(assignment), **element)
