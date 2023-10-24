from rest_framework import serializers
from rest_framework.serializers import ValidationError

from ...models import User


class UserSerializers(serializers.ModelSerializer):
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

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError({"Password error": "Passoword do no match."})

        return attrs

    def create(self, validated_data):
        """Pop the confirm password fields during create an user."""

        validated_data.pop("confirm_password", None)
        return super().create(validated_data)
