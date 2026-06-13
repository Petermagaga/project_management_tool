from rest_framework import serializers

from .models import Comment


class CommentSerializer(
    serializers.ModelSerializer
):

    user_email = serializers.CharField(
        source="user.email",
        read_only=True
    )

    class Meta:

        model = Comment

        fields = [

            "id",
            "task",
            "user",
            "user_email",
            "content",
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "user",
            "created_at",
            "updated_at",
        )