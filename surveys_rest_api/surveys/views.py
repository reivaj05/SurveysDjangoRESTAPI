from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from common.permissions import BelongToUser
from .models import QuestionType, Section, Survey
from .serializers import (
    QuestionTypeSerializer, SectionSerializer,
    SurveySerializer, SurveySerializerPut
)


class SurveyViewSet(viewsets.ModelViewSet):
    permission_classes = (
        # permissions.IsAuthenticated,
        # BelongToUser,
    )
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        # queryset = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = SurveySerializerPut
        return serializer_class


class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def list(self, request, survey_pk=None):
        queryset = self.queryset.filter(survey=survey_pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, survey_pk=None):
        section = get_object_or_404(self.queryset, pk=pk, survey=survey_pk)
        serializer = self.serializer_class(section)
        return Response(serializer.data)


class QuestionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
