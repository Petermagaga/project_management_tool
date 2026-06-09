from rest_framework import serializers

from .models import (
    Workspace,WorkspaceMember
)


class WorkspaceSerializers(serializers.Serializer):
    owner=serializers.StringRelatedField()
    class Meta:
        model=Workspace
        fields="__all__"
        read_only_fields=("owner")

class WorkspaceMemberSerializer(serializers.Serializer):
    user_email=serializers.CharField(source="user.email",read_only=True)
    
    class Meta:
        model=WorkspaceMember,
        fields="__all__"
    