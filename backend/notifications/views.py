from rest_framework.views import APIView

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response

from .models import ActivityLog

from .serializers import (
    ActivityLogSerializer
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