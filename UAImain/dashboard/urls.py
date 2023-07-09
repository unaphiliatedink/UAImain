from django.urls import path
from .views import dashHome, announcementDetail, announcementUpdate, AnnouncementDeleteView
from . import views


urlpatterns = [
    path('', dashHome.as_view(), name='dashboard'),
    path('announcement/<int:pk>', views.announcementDetail.as_view(), name='announcement_detail'),
    path('announcement/<pk>/update', views.announcementUpdate.as_view(), name='announcement_update'),
    path('announcement/<pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),
]