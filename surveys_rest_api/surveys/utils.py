from rest_framework import serializers
from .models import (
    Option, Question, Section, Survey
)


def update_sections(sections_data, survey):
    for section in sections_data:
        # Get the questions data for each section
        questions_data = section.pop('questions')

        # If the section already exists in the DB, just update their values
        # otherwise we create a new section
        try:
            section_db = Section.objects.get(id=section.pop('id'))
            # Check if the section belongs to the survey
            check_owner(
                section_db.survey,
                survey,
                'Not your section, we do not allow it'
            )
            # Update the section from the db with the new values
            section_db = update_instance(section_db, section)
        except Section.DoesNotExist:
            Section.objects.create(survey=survey, **section)


def check_owner(instance_db, instance, message):
    if instance_db != instance:
        raise serializers.ValidationError(message)


def update_instance(instance, new_data):
    instance = unpack_values(instance, new_data)
    instance.save()
    return instance


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
    # Get the sections to update from the request
    sections_data = validated_data.pop('sections')

    # Get survey data and update it
    survey = update_instance(survey, validated_data)

    # Get the sections from the db to check which were deleted
    sections_db = survey.sections.all()

    delete_sections(sections_db, sections_data)
    update_sections(sections_data, survey)

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
