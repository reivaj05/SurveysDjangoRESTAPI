from django.conf.urls import url, include


urlpatterns = [
    url(r'^surveys/', include('surveys.urls'))
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
