from django.urls import path

from .views import (
    ProjectActivityFeedView
)

urlpatterns = [

    path(
        "project/<int:project_id>/",
        ProjectActivityFeedView.as_view()
    ),
]