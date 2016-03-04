from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import RequestFactory, TestCase
from .models import UserProfile
from .views import UserProfileDetailView


class TestUserProfileDetailView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user_profile_url = reverse('accounts:user_profile')
        authentication_user = User.objects.create_user(
            username='test_user',
            email='test_email@test.com',
            password='test_password',
            first_name='test_first_name',
            last_name='test_last_name'
        )
        self.user = UserProfile.objects.create(
            authentication_user=authentication_user
        )

    def test_view_with_valid_user(self):
        request = self.factory.get(self.user_profile_url)
        request.user = self.user.authentication_user
        response = UserProfileDetailView.as_view()(request)
        self.assertEqual(
            response.status_code,
            200,
            'Expected status code to be equal to 200'
        )

    def test_template(self):
        request = self.factory.get(self.user_profile_url)
        request.user = self.user.authentication_user
        response = UserProfileDetailView.as_view()(request)
        self.assertTemplateUsed(
            response=response,
            template_name='account/user_profile.html',
            msg_prefix='Expected template used to be user_profile.html',
        )

    def test_context_object_name(self):
        view = UserProfileDetailView()
        self.assertEqual(
            view.context_object_name,
            'user_profile',
            'Expected context object name to be user_profile',
        )

    def test_context_object(self):
        request = self.factory.get(self.user_profile_url)
        request.user = self.user.authentication_user
        response = UserProfileDetailView.as_view()(request)
        context_user_profile = response.context_data['user_profile']
        # context_user_accounts = response.context_data['user_accounts']
        self.assertEqual(
            self.user,
            context_user_profile,
            'Expected context user profile to be equal to db user profile'
        )
