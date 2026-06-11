from django.urls import path
from .views import (CreateProjectView,WorkspaceProjectsView,ProjectDetailView,UpdateProjectView,DeleteProjectView)

urlpatterns = [
    path("create/",CreateProjectView.as_view()),
    path("workspace/<int:workspace_id>/",WorkspaceProjectsView.as_view()),
    path("<int:project_id>/",ProjectDetailView.as_view()),
    path("<int:project_id>/update/",UpdateProjectView.as_view()),
    path("<int:project_id>/delete/",DeleteProjectView.as_view()),
]
