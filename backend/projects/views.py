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

from notifications.services import (
    create_activity_log
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
    
        project = serializer.save(
            created_by=self.request.user
        )

        create_activity_log(
            project=project,
            user=self.request.user,
            action_type="PROJECT_CREATED",
            message=f"{self.request.user.username} created project '{project.name}'"
        )



class WorkspaceProjectsView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        workspace_id
    ):

        projects = Project.objects.filter(
            workspace_id=workspace_id
        )

        serializer = ProjectSerializer(
            projects,
            many=True
        )

        return Response(
            serializer.data
        )
    

class ProjectDetailView(APIView):

    permission_classes = [
        IsAuthenticated]

    def get(self,request,project_id):

        project = get_object_or_404(
            Project,
            id=project_id
        )

        serializer = ProjectSerializer(
            project
        )

        return Response(
            serializer.data
        )


class UpdateProjectView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request,
        project_id
    ):

        project = get_object_or_404(
            Project,
            id=project_id
        )

        serializer = ProjectSerializer(
            project,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )
    

class DeleteProjectView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        project_id
    ):

        project = get_object_or_404(
            Project,
            id=project_id
        )

        project.delete()

        return Response(
            {
                "message":
                "Project deleted"
            }
        )