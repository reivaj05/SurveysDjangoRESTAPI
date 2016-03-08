from rest_framework import permissions
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
