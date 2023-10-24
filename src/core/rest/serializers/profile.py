from rest_framework import serializers

from core.models import User

from core.validationsMixin import UserCommonValidationMixin


class UserDetailSerializer(UserCommonValidationMixin, serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "uid",
            "phone",
            "first_name",
            "last_name",
            "slug",
            "nid",
            "image",
            "type",
            "status",
            "gender",
            "date_of_birth",
            "height",
            "weight",
            "blood_group",
            "password",
            "confirm_password",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["uid", "slug", "status", "created_at", "updated_at"]

