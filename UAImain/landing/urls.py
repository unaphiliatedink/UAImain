from django.urls import path
from .views import Index
from . import views


urlpatterns = [
    path('', Index.as_view(), name='index'),
]