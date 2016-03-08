# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            'id', 'title', 'description', 'created_at',
            'updated_at', 'active',
        )

        read_only_fields = ('created_at', 'updated_at', 'active')
