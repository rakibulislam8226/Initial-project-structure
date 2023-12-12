from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.models import User

from core.validationsMixin import UserCommonValidationMixin


class PublicUserListSerializers(UserCommonValidationMixin, serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    nid = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.filter(),
                message="NID already exists. Please choose a different one.",
            )
        ],
        required=False,
        allow_null=True,
    )

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
        validated_data.pop("confirm_password", None)
        return super().create(validated_data)
