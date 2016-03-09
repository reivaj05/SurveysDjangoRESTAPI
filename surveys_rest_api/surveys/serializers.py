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


def update_sections(sections_data, survey):

    print '***************'
    print sections_data
    print '***************'
    for section in sections_data:
        questions_data = section.pop('questions')
        try:
            section_db = Section.objects.get(id=section.pop('id'))
            if section_db.survey != survey:
                raise serializers.ValidationError(
                    'Not your section, we do not allow it'
                )
            section_db = unpack_values(section_db, section)
            section_db.save()
        except Section.DoesNotExist:
            Section.objects.create(survey=survey, **section)


def unpack_values(instance, new_data):
    for attr, value in new_data.items():
        setattr(instance, attr, value)
    return instance


def delete_sections(sections_db, sections_data):
    ids = [value.get('id') for value in sections_data]
    for section in sections_db:
        if section.id not in ids:
            section.delete()


def update_survey(survey, validated_data):
    survey.title = validated_data.get('title', survey.title)
    survey.description = validated_data.get(
        'description', survey.description
    )
    survey.active = validated_data.get('active', survey.active)
    sections_data = validated_data.pop('sections')
    sections_db = survey.sections.all()
    delete_sections(sections_db, sections_data)
    update_sections(sections_data, survey)

    survey.save()
    return None
    # return survey


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
