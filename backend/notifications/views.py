from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response

from .models import ActivityLog, Notification

from .serializers import (
    ActivityLogSerializer,NotificationSerializer
)


class ProjectActivityFeedView(
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

        activities = ActivityLog.objects.filter(
            project_id=project_id
        )

        serializer = ActivityLogSerializer(
            activities,
            many=True
        )

        return Response(
            serializer.data
        )
    

class UserNotificationsView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        notifications = (
            Notification.objects.filter(
                recipient=request.user
            )
        )

        serializer = (
            NotificationSerializer(
                notifications,
                many=True
            )
        )

        return Response(
            serializer.data
        )
    

class MarkNotificationReadView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request,
        notification_id
    ):

        notification = get_object_or_404(

            Notification,

            id=notification_id,

            recipient=request.user
        )

        notification.is_read = True

        notification.save()

        return Response(
            {
                "message":
                "Notification marked read"
            }
        )
    

class MarkNotificationReadView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request,
        notification_id
    ):

        notification = get_object_or_404(

            Notification,

            id=notification_id,

            recipient=request.user
        )

        notification.is_read = True

        notification.save()

        return Response(
            {
                "message":
                "Notification marked read"
            }
        )
    
class UnreadNotificationCountView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        count = Notification.objects.filter(

            recipient=request.user,

            is_read=False

        ).count()

        return Response(
            {
                "unread_count": count
            }
        )
