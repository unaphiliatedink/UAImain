from django.urls import path
from .views import Index, contactPageView
from . import views


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', contactPageView.as_view(), name='contact'),
    
    
]