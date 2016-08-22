from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response
# from common.permissions import BelongToUser
from .models import (
    Answer, Option, Question,
    QuestionType, Section, Survey
)
from .serializers import (
    AnswerSerializer, OptionSerializer, QuestionSerializer,
    QuestionTypeSerializer, SectionSerializer, SurveySerializer,
    SurveySerializerPut,
)


class SurveyViewSet(viewsets.ModelViewSet):
    permission_classes = (
        # permissions.IsAuthenticated,
        # BelongToUser,
    )
    queryset = Survey.objects
    serializer_class = SurveySerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = SurveySerializerPut
        return serializer_class

    def list(self, request):
        # queryset = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )
    queryset = Section.objects
    serializer_class = SectionSerializer

    def list(self, request):
        try:
            survey = self._get_survey(request)
            return self._send_results(survey)
        except Exception, error:
            return Response({
                'error': str(error)
            })

    def _get_survey(self, request):
        survey_id = request.query_params.get("survey_id")
        if not survey_id:
            raise Exception("Survey id not passed")
        return get_object_or_404(Survey, pk=survey_id)

    def _send_results(self, survey):
        queryset = self.queryset.filter(survey=survey)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, survey_pk=None):
        # section = get_object_or_404(self.queryset, pk=pk, survey=survey_pk)
        section = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(section)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )
    queryset = Question.objects
    serializer_class = QuestionSerializer

    def list(self, request, survey_pk=None):
        # queryset = self.queryset.filter(survey=survey_pk)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, survey_pk=None):
        # section = get_object_or_404(self.queryset, pk=pk, survey=survey_pk)
        section = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(section)
        return Response(serializer.data)


class QuestionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer


class OptionViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )
    queryset = Option.objects
    serializer_class = OptionSerializer

    def list(self, request, survey_pk=None):
        # queryset = self.queryset.filter(survey=survey_pk)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, survey_pk=None):
        # section = get_object_or_404(self.queryset, pk=pk, survey=survey_pk)
        section = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(section)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )
    queryset = Answer.objects
    serializer_class = AnswerSerializer

    def list(self, request, survey_pk=None):
        # queryset = self.queryset.filter(survey=survey_pk)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, survey_pk=None):
        # section = get_object_or_404(self.queryset, pk=pk, survey=survey_pk)
        section = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(section)
        return Response(serializer.data)
