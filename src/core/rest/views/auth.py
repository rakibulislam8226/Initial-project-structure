from rest_framework import generics, permissions

from ..serializers.auth import UserSerializers

from ...models import User


class PatientAuthView(generics.CreateAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny]
