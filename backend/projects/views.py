from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response

from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from workspaces.models import (
    Workspace
)

from workspaces.permissions import (
    get_user_role
)

from .models import (
    Project
)

from .serializers import (
    ProjectSerializer
)


class CreateProjectView(
    generics.CreateAPIView
):

    serializer_class = ProjectSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(
        self,
        serializer
    ):

        workspace_id = self.request.data.get(
            "workspace"
        )

        workspace = get_object_or_404(
            Workspace,
            id=workspace_id
        )

        role = get_user_role(
            self.request.user,
            workspace
        )

        if role not in [
            "OWNER",
            "ADMIN"
        ]:
            raise PermissionError(
                "Permission denied"
            )

        serializer.save(
            created_by=self.request.user
        )
