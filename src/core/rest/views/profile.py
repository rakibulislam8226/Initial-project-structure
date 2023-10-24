from rest_framework import generics

from core.models import User

from ..serializers.profile import UserDetailSerializer
from ..permissions import IsOwnerOrReadOnly


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.filter()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user
