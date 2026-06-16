from rest_framework import serializers

from .models import Task,TaskAttachment


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

class TaskAttachmentSerializer(
    serializers.ModelSerializer
):

    uploaded_by_email = serializers.CharField(
        source="uploaded_by.email",
        read_only=True
    )

    class Meta:

        model = TaskAttachment

        fields = "__all__"

        read_only_fields = (
            "uploaded_by",
            "uploaded_at",
        )