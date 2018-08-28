
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views_api import CreateItemPostAPI

app_name = '_api'

urlpatterns = [
    path('api/main/add/items', CreateItemPostAPI, name='api-add-item'),
]
