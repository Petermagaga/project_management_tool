from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from tasks.models import Task

from .models import Comment
from .serializers import CommentSerializer


class CreateCommentView(
    generics.CreateAPIView
):

    serializer_class = CommentSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            user=self.request.user
        )


class TaskCommentsView(
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

        comments = Comment.objects.filter(
            task_id=task_id
        ).order_by(
            "created_at"
        )

        serializer = CommentSerializer(
            comments,
            many=True
        )

        return Response(
            serializer.data
        )
    
class UpdateCommentView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request,
        comment_id
    ):

        comment = get_object_or_404(
            Comment,
            id=comment_id
        )

        if comment.user != request.user:

            return Response(
                {
                    "error":
                    "You can only edit your own comments"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CommentSerializer(
            comment,
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

class DeleteCommentView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        comment_id
    ):

        comment = get_object_or_404(
            Comment,
            id=comment_id
        )

        if comment.user != request.user:

            return Response(
                {
                    "error":
                    "You can only delete your own comments"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        comment.delete()

        return Response(
            {
                "message":
                "Comment deleted"
            }
        )
