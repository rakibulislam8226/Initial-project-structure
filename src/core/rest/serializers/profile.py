from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.models import User

from core.validationsMixin import UserCommonValidationMixin


class UserDetailSerializer(UserCommonValidationMixin, serializers.ModelSerializer):
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
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["uid", "slug", "status", "created_at", "updated_at"]
