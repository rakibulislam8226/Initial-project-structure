from django.urls import path

from ..views.auth import PatientAuthView

urlpatterns = [
    path("", PatientAuthView.as_view(), name="core.auth"),
]
