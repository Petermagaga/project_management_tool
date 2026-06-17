from django.urls import path

from .views import (

    CreateTaskView,

    BoardTasksView,

    TaskDetailView,

    UpdateTaskView,

    DeleteTaskView,
    TaskAttachmentsView,DeleteAttachmentView,UploadAttachmentView,
)

urlpatterns = [

    path(
        "create/",
        CreateTaskView.as_view()
    ),

    path(
        "board/<int:board_id>/",
        BoardTasksView.as_view()
    ),

    path(
        "<int:task_id>/",
        TaskDetailView.as_view()
    ),

    path(
        "<int:task_id>/update/",
        UpdateTaskView.as_view()
    ),

    path(
        "<int:task_id>/delete/",
        DeleteTaskView.as_view()
    ),

    path(
        "attachment/upload/",
        UploadAttachmentView.as_view()
    ),

    path(
        "attachment/task/<int:task_id>/",
        TaskAttachmentsView.as_view()
    ),

    path(
        "attachment/<int:attachment_id>/delete/",
        DeleteAttachmentView.as_view()
    ),

]