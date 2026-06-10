from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response

from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from accounts.models import User

from .models import (
    Workspace,
    WorkspaceMember
)

from .serializers import (
    WorkspaceSerializer,
    WorkspaceMemberSerializer
)



class CreateWorkspaceView(
    generics.CreateAPIView
):

    serializer_class = WorkspaceSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(
        self,
        serializer
    ):

        workspace = serializer.save(
            owner=self.request.user
        )

        WorkspaceMember.objects.create(
            workspace=workspace,
            user=self.request.user,
            role="OWNER"
        )



class WorkspaceListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        workspaces = Workspace.objects.filter(
            members__user=request.user
        )

        serializer = WorkspaceSerializer(
            workspaces,
            many=True
        )

        return Response(
            serializer.data
        )
    
class InviteMemberView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        workspace_id
    ):

        workspace = get_object_or_404(
            Workspace,
            id=workspace_id
        )

        email = request.data.get(
            "email"
        )

        role = request.data.get(
            "role",
            "MEMBER"
        )

        user = get_object_or_404(
            User,
            email=email
        )

        WorkspaceMember.objects.get_or_create(
            workspace=workspace,
            user=user,
            defaults={
                "role": role
            }
        )

        return Response(
            {
                "message":
                "Member invited"
            }
        )
    

class WorkspaceMembersView(
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

        members = WorkspaceMember.objects.filter(
            workspace_id=workspace_id
        )

        serializer = WorkspaceMemberSerializer(
            members,
            many=True
        )

        return Response(
            serializer.data
        )