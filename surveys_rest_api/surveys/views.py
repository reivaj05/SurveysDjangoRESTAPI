from rest_framework import permissions
from rest_framework import viewsets
from common.permissions import IsOwnerOrReadOnly
from .models import Survey
from .serializers import SurveySerializer


class SurveyViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
