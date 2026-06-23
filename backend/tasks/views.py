from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response

from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from boards.models import Board

from .models import Task,TaskAttachment

from .serializers import TaskSerializer,TaskAttachmentSerializer



from notifications.services import (
    create_activity_log,create_notification
)

class CreateTaskView(
    generics.CreateAPIView
):

    serializer_class = TaskSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(
        self,
        serializer
    ):

        task = serializer.save(
            reporter=self.request.user
        )


        if task.assignee:

            create_notification(

                recipient=task.assignee,

                sender=self.request.user,

                notification_type="TASK_ASSIGNED",

                message=(
                    f"You were assigned "
                    f"'{task.title}'"
                )
            )

        create_activity_log(

            project=task.project,

            user=self.request.user,

            action_type="TASK_CREATED",

            message=(
                f"{self.request.user.username} "
                f"created task '{task.title}'"
            )
        )


class BoardTasksView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        board_id
    ):

        tasks = Task.objects.filter(
            board_id=board_id
        )

        serializer = TaskSerializer(
            tasks,
            many=True
        )

        return Response(
            serializer.data
        )
    

class TaskDetailView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        task_id
    ):

        task = get_object_or_404(
            Task,
            id=task_id
        )

        serializer = TaskSerializer(
            task
        )

        return Response(
            serializer.data
        )
    

class UpdateTaskView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request,
        task_id
    ):

        task = get_object_or_404(
            Task,
            id=task_id
        )

        serializer = TaskSerializer(
            task,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )
        old_board=task.board
        
        serializer.save()
        task.refresh_from_db()
        if old_board !=task.board:
            create_activity_log(
                project=task.project,
                user=request.user,
                action_type="TASK_MOVED",
                message=(
                    f"{request.user.username}"
                    f"moved task '{task.title}'"
                    f"to'{task.board.name}'"
                )
            )
        return Response(serializer.data)
    

class DeleteTaskView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        task_id
    ):

        task = get_object_or_404(
            Task,
            id=task_id
        )

        task.delete()

        return Response(
            {
                "message":
                "Task deleted"
            }
        )
    
    

class UploadAttachmentView(
    generics.CreateAPIView
):

    serializer_class = (
        TaskAttachmentSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(
        self,
        serializer
    ):

        uploaded_file = (
            self.request.FILES["file"]
        )

        attachment = serializer.save(

            uploaded_by=self.request.user,

            original_filename=uploaded_file.name
        )

        create_activity_log(

            project=attachment.task.project,

            user=self.request.user,

            action_type="TASK_UPDATED",

            message=(
                f"{self.request.user.username} "
                f"uploaded file "
                f"'{uploaded_file.name}'"
            )
        )


class TaskAttachmentsView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        task_id
    ):

        attachments = (
            TaskAttachment.objects.filter(
                task_id=task_id
            )
        )

        serializer = (
            TaskAttachmentSerializer(
                attachments,
                many=True
            )
        )

        return Response(
            serializer.data
        )

class DeleteAttachmentView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        attachment_id
    ):

        attachment = get_object_or_404(

            TaskAttachment,

            id=attachment_id
        )

        attachment.delete()

        return Response(
            {
                "message":
                "Attachment deleted"
            }
        )


class ProjectTaskView(generics.ListAPIView):

    serializer_class= (TaskSerializer)

    permission_classes=[
        IsAuthenticated
    ]

    def get_queryset(self):
        project_id=(
            self.kwargs["project_id"]
        )

        return Task.objects.filter(project_id=project_id
                                   ).select_related(
                                       "board",
                                       "assignee",
                                       "reporter"
                                   )