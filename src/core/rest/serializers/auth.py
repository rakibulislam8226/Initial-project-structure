from rest_framework import serializers

from core.models import User

from core.validationsMixin import UserCommonValidationMixin


class UserSerializers(UserCommonValidationMixin, serializers.ModelSerializer):
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

    def create(self, validated_data):
        """Pop the confirm password fields during create an user."""

        validated_data.pop("confirm_password", None)
        return super().create(validated_data)
