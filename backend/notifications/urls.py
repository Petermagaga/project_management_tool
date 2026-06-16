from django.urls import path

from .views import (

    ProjectActivityFeedView,

    UserNotificationsView,

    MarkNotificationReadView,

    UnreadNotificationCountView
)

urlpatterns = [

    path(
        "project/<int:project_id>/",
        ProjectActivityFeedView.as_view()
    ),

    path(
        "notifications/",
        UserNotificationsView.as_view()
    ),

    path(
        "notifications/count/",
        UnreadNotificationCountView.as_view()
    ),

    path(
        "notifications/<int:notification_id>/read/",
        MarkNotificationReadView.as_view()
    ),
]