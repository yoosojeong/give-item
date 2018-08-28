from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = '_give'

urlpatterns = []

urlpatterns += [
    # url(
    #     regex=r'main/',
    #     view=Main.as_view(),
    #     name='main',
    # ),
    url(
        regex=r'^main/items/$',
        view=Item.as_view(),
        name='list-item',
    ),
    url(
        regex=r'^main/add/items$',
        view=ItemAdd.as_view(),
        name='add-item',
    ),
    # url(
    #     regex=r'^main/items/(?P<item_id>[0-9]+)/$',
    #     view=ItemDetail.as_view(),
    #     name='detail-item',
    # ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(
        regex=r'^signup/$',
        view=SignUp.as_view(),
        name='signup',
    ),
]

