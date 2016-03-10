from rest_framework import serializers
from .models import (
    Option, Question, Section, Survey
)


def update_options(options_data, question):
    # delete_instances(question.options.all(), options_data)
    # for option in options_data:

    #     option_db = Option.objects.filter(id=option.pop('id')).first()
    #     owner = (option_db.question if hasattr(option_db, 'question')
    #              else None)

    #     update_data_survey(
    #         option,
    #         option_db,
    #         Option,
    #         'finish',
    #         owner,
    #         question,
    #         'Not your option, we do not allow it',
    #         None,
    #         None,
    #         question=question
    #     )
    pass


def update_questions(questions_data, section):
    delete_instances(section.questions.all(), questions_data)
    for question in questions_data:

        question_db = Question.objects.filter(id=question.pop('id')).first()
        owner = (question_db.section if hasattr(question_db, 'section')
                 else None)

        update_data_survey(
            question, question_db, Question, 'options', owner,
            section, 'Not your question, we do not allow it',
            update_options, create_options, section=section
        )


def update_sections(sections_data, survey):
    delete_instances(survey.sections.all(), sections_data)
    for section in sections_data:

        section_db = Section.objects.filter(id=section.pop('id')).first()
        owner = section_db.survey if hasattr(section_db, 'survey') else None

        update_data_survey(
            section, section_db, Section, 'questions',
            owner, survey, 'Not your section, we do not allow it',
            update_questions, create_questions, survey=survey
        )


def update_data_survey(
        element, element_db, model, next_data_key,
        owner, expected_owner, not_allow_message,
        next_update, next_create, **kwargs):
    next_data = element.pop(next_data_key)
    if element_db:

        check_owner(
            owner,
            expected_owner,
            not_allow_message
        )

        element_db = update_instance(element_db, element)
        if next_data:
            next_update(next_data, element_db)
    else:
        kwargs = dict(element.items() + kwargs.items())
        element_created = model.objects.create(**kwargs)
        if next_data:
            next_create(next_data, element_created)


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


def delete_instances(instances_db, instances_data):
    ids = [value.get('id') for value in instances_data]
    for instance in instances_db:
        if instance.id not in ids:
            instance.delete()


def update_survey(survey, validated_data):
    # Get the sections to update from the request
    sections_data = validated_data.pop('sections')

    # Get survey data and update it
    survey = update_instance(survey, validated_data)

    # Start updating the survey, first the sections
    update_sections(sections_data, survey)

    return None
    # return survey


def create_options(options_data, question_created):
    for option in options_data:
        check_if_has_id(option)
        Option.objects.create(question=question_created, **option)


def create_questions(questions_data, section_created):
    for question in questions_data:
        check_if_has_id(question)
        options_data = question.pop('options')
        question_type = question.pop('question_type')
        question_created = Question.objects.create(
            section=section_created,
            question_type=question_type,
            **question
        )
        create_options(options_data, question_created)


def check_if_has_id(element):
    try:
        element.pop('id')
    except:
        pass


def create_sections(sections_data, survey_created):
    for section in sections_data:
        check_if_has_id(section)
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
