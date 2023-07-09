from django.urls import path
from .views import servicesIndex, Piercings, Tattoos, Microblading, Pmu

urlpatterns = [
    path('', servicesIndex.as_view(), name='services_index'),
    path('piercings/', Piercings.as_view(), name='piercings'),
    path('tattoos/', Tattoos.as_view(), name='tattoos'),
    path('micro-blading/', Microblading.as_view(), name='micro-blading'),
    path('pmu/', Pmu.as_view(), name='pmu'),
]
