from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PhysicianListView, PatientListView

urlpatterns = [
    path('doclist', PhysicianListView.as_view(), name="doclist"),
    path('patientlist', PatientListView.as_view(), name="patientlist"),
    re_path(r'^patientlist/(?P<pk>[0-9]+)$', PatientListView.as_view(), name="patientlist")
]
