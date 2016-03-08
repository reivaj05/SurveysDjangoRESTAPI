# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id', 'email', 'username', 'date_joined',
            'updated_at', 'first_name', 'last_name',
            'birthday', 'gender', 'id_network',
            'biography', 'image_profile', 'password',
        )

        read_only_fields = ('date_joined', 'updated_at')

    def create(self, validated_data):
        user = UserProfile.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

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
