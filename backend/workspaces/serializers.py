from rest_framework import serializers

from .models import (
    Workspace,
    WorkspaceMember
)


class WorkspaceSerializer(
    serializers.ModelSerializer
):
    owner = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Workspace
        fields = "__all__"
        read_only_fields = (
            "owner",
        )


class WorkspaceMemberSerializer(
    serializers.ModelSerializer
):
    user_email = serializers.CharField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = WorkspaceMember
        fields = "__all__"