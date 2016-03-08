# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Question, Section, Survey


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'hint', 'required', 'question_type',)


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
            'id', 'title', 'description', 'created_at',
            'updated_at', 'active', 'sections', 'user'
        )

        read_only_fields = ('created_at', 'updated_at', 'active', 'user')

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        survey = Survey.objects.create(**validated_data)
        for section in sections_data:
            Section.objects.create(survey=survey, **section)

        # self.create_data(sections_data, Section, 'survey=fk', survey)
        return survey

    def create_data(self, data, model, assignment, fk):
        print eval(assignment)
        for element in data:
            model.objects.create(eval(assignment), **element)
