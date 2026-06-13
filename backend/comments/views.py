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