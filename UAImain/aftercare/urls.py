from django.urls import path
from .views import afterCare
from . import views


urlpatterns = [
    path('', afterCare.as_view(), name='aftercare'),

]