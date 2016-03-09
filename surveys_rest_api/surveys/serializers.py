# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import (
    Answer, Option, Question, QuestionType, Section, Survey
)
from .utils import create_survey, update_survey


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


class SectionSerializerPut(SectionSerializer):
    id = serializers.IntegerField(required=True)


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

    def update(self, survey, validated_data):
        return update_survey(survey, validated_data)
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        # print sections_data.filter(id=15)
        # profile.is_premium_member = profile_data.get(
        #     'is_premium_member',
        #     profile.is_premium_member
        # )
        # profile.has_support_contract = profile_data.get(
        #     'has_support_contract',
        #     profile.has_support_contract
        # )
        # profile.save()

        return survey


class SurveySerializerPut(SurveySerializer):
    sections = SectionSerializerPut(many=True)
