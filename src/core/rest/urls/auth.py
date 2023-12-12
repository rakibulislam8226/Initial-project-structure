from django.urls import path

from ..views.auth import PublicUserAuthView

urlpatterns = [
    path("", PublicUserAuthView.as_view(), name="core.user-auth"),
]
