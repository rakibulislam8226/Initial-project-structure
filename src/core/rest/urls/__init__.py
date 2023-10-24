from django.urls import path, include

urlpatterns = [
    path("/profile", include("core.rest.urls.profile")),
    path("/auth", include("core.rest.urls.auth")),
]
