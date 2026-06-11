from django.urls import path

from .views import (CreateBoardView,ProjectBoardsView,

    BoardDetailView,

    UpdateBoardView,

    DeleteBoardView
)

urlpatterns = [

    path(
        "create/",
        CreateBoardView.as_view()
    ),

    path(
        "project/<int:project_id>/",
        ProjectBoardsView.as_view()
    ),

    path(
        "<int:board_id>/",
        BoardDetailView.as_view()
    ),

    path(
        "<int:board_id>/update/",
        UpdateBoardView.as_view()
    ),

    path(
        "<int:board_id>/delete/",
        DeleteBoardView.as_view()
    ),
]