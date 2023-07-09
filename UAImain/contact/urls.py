from django.urls import path
from .views import contactPageView, contactDetail, contactSuccessful, contactDeleteView
from . import views


urlpatterns = [
    path('', views.contactPageView.as_view(), name='contact'),
    path('detail/<int:pk>', views.contactDetail.as_view(), name='contact_detail'),
    path('detail/<pk>/contact_successful', contactSuccessful.as_view(), name='contact_success'),
    path('<pk>/delete/', contactDeleteView.as_view(), name='contact_delete'),
    
    # Forms paths
    path('form', views.contact_form, name='form'),
]