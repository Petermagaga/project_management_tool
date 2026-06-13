from django.urls import path

from .views import (

    CreateCommentView,TaskCommentsView,UpdateCommentView,
    DeleteCommentView
)

urlpatterns = [

    path(
        "create/",
        CreateCommentView.as_view()
    ),

    path(
        "task/<int:task_id>/",
        TaskCommentsView.as_view()
    ),

    path(
        "<int:comment_id>/update/",
        UpdateCommentView.as_view()
    ),

    path(
        "<int:comment_id>/delete/",
        DeleteCommentView.as_view()
    ),
]