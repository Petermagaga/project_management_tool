from django.urls import path

from .views import (

    CreateWorkspaceView,

    WorkspaceListView,

    InviteMemberView,

    WorkspaceMembersView
)

urlpatterns = [

    path(
        "",
        WorkspaceListView.as_view()
    ),

    path(
        "create/",
        CreateWorkspaceView.as_view()
    ),

    path(
        "<int:workspace_id>/invite/",
        InviteMemberView.as_view()
    ),

    path(
        "<int:workspace_id>/members/",
        WorkspaceMembersView.as_view()
    ),
]