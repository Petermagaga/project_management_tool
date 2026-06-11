from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from projects.models import Project
from .models import Board
from .serializers import BoardSerializer

class CreateBoardView(generics.CreateAPIView):
    serializer_class=BoardSerializer
    permission_classes=[IsAuthenticated]


class ProjectBoardsView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        project_id
    ):

        boards = Board.objects.filter(
            project_id=project_id
        )

        serializer = BoardSerializer(
            boards,
            many=True
        )

        return Response(
            serializer.data
        )


class BoardDetailView(
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

        board = get_object_or_404(
            Board,
            id=board_id
        )

        serializer = BoardSerializer(
            board
        )

        return Response(
            serializer.data
        )
    

class UpdateBoardView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request,
        board_id
    ):

        board = get_object_or_404(
            Board,
            id=board_id
        )

        serializer = BoardSerializer(
            board,
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
    

class DeleteBoardView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        board_id
    ):

        board = get_object_or_404(
            Board,
            id=board_id
        )

        board.delete()

        return Response(
            {
                "message":
                "Board deleted"
            }
        )