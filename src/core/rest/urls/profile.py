from django.urls import path

from ..views.profile import UserProfileDetailView

urlpatterns = [
    path("", UserProfileDetailView.as_view(), name="core.user-profile"),
]
