from django.conf.urls import url, include
from rest_framework_nested import routers
from accounts.views import UserProfileViewSet
from surveys.views import SectionViewSet, SurveyViewSet

router = routers.DefaultRouter()
router.register(r'accounts', UserProfileViewSet)
router.register(r'surveys', SurveyViewSet)

surveys_router = routers.NestedSimpleRouter(
    router, r'surveys', lookup='survey'
)
surveys_router.register(
    r'sections', SectionViewSet, base_name='survey-sections'
)
# router.register(r'surveys/(?P<pk>[0-9]+)/sections', SectionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(surveys_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # url(r'^$', IndexView.as_view(), name='index'),
    # url(
    #     r'^(?P<venue_id>[0-9]+)/menu-detail/(?P<pk>[0-9]+)$',
    #     MenuDetailView.as_view(),
    #     name='menu_detail'
    # ),
    # url(
    #     r'^(?P<venue_id>[0-9]+)/menu-create/$',
    #     MenuCreateView.as_view(),
    #     name='menu_create'
    # ),
    # url(
    #     r'^(?P<venue_id>[0-9]+)/menu-list/$',
    #     MenuListView.as_view(),
    #     name='menu_list'
    # ),
    # url(
    #     r'^(?P<venue_id>[0-9]+)/menu-update/(?P<pk>[0-9]+)$',
    #     MenuUpdateView.as_view(),
    #     name='menu_update'
    # ),
    # url(
    #     r'^(?P<venue_id>[0-9]+)/menu-delete/(?P<pk>[0-9]+)/$',
    #     MenuDeleteView.as_view(),
    #     name='menu_delete'
    # ),
]
