from rest_framework import serializers

from .models import Task


class TaskSerializer(
    serializers.ModelSerializer
):

    assignee_email = serializers.CharField(
        source="assignee.email",
        read_only=True
    )

    reporter_email = serializers.CharField(
        source="reporter.email",
        read_only=True
    )

    class Meta:

        model = Task

        fields = "__all__"

        read_only_fields = (
            "reporter",
        )