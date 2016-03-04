from django.conf.urls import url
from .views import UserProfileDetailView

urlpatterns = [
    url(r'^profile/$', UserProfileDetailView.as_view(), name='user_profile'),
]
