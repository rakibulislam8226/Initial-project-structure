from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from ..serializers.auth import PublicUserListSerializers

from ...models import User


class PublicUserAuthView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return Response(
                {"error": "You are not allowed to access this endpoint."},
                status=403,
            )
        return Response({"message": "This is a GET request for unauthenticated users."})

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return Response(
                {"error": "You are not allowed to access this endpoint."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = PublicUserListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
