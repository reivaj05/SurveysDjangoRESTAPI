from django.views.generic import DetailView
from common.mixins import LoginRequiredMixin
from .models import UserProfile
# Create your views here.


class UserProfileDetailView(LoginRequiredMixin, DetailView):
        template_name = 'account/user_profile.html'
        context_object_name = 'user_profile'

        def get_object(self, queryset=None):
            authentication_user = self.request.user
            user, created = UserProfile.objects.get_or_create(
                authentication_user=authentication_user
            )
            return user

        def get_context_data(self, **kwargs):
            context = super(UserProfileDetailView, self).get_context_data(
                **kwargs
            )
            user = self.request.user
            context['user_accounts'] = user.socialaccount_set.all()
            return context
