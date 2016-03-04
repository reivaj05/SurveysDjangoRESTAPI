from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name'
        ]

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def signup(self, request, user):
        user.save()
        UserProfile.objects.create(authentication_user=user)
