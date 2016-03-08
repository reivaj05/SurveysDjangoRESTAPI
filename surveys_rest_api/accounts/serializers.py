# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from surveys.serializers import SurveySerializer
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=False)
    # confirm_password = serializers.CharField(write_only=True, required=False)

    surveys = SurveySerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = UserProfile
        fields = (
            'id', 'email', 'username', 'date_joined',
            'updated_at', 'first_name', 'last_name',
            'birthday', 'gender', 'id_network',
            'biography', 'image_profile', 'surveys',
            # 'password', 'confirm_password',
        )

        read_only_fields = ('date_joined', 'updated_at')

        # def create(self, validated_data):
        #     return UserProfile.objects.create(**validated_data)

        # def update(self, instance, validated_data):
        #     instance.username = validated_data.get(
        #         'username', instance.username
        #     )
        #     instance.tagline = validated_data.get(
        #         'tagline', instance.tagline
        #     )

        #     instance.save()

        #     # password = validated_data.get('password', None)
        #     # confirm_password = validated_data.get('confirm_password', None)

        #    # if password and confirm_password and password==confirm_password:
        #     #     instance.set_password(password)
        #     #     instance.save()

        #     # update_session_auth_hash(self.context.get('request'), instance)

        #     return instance
