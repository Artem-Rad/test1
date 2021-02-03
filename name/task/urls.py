from django.urls import path
from .views import name, json_name


urlpatterns = [
    path('', name, name='name'),
    path('json', json_name, name='json')
]
