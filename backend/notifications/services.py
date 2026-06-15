from .models import ActivityLog

from rest_framework.views import APIView

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response

from .serializers import (
    ActivityLogSerializer
)

def create_activity_log(

    project,

    user,

    action_type,

    message

):

    ActivityLog.objects.create(

        project=project,

        user=user,

        action_type=action_type,

        message=message
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
