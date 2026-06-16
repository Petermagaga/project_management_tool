from rest_framework import serializers

from .models import ActivityLog,Notification


class ActivityLogSerializer(
    serializers.ModelSerializer
):

    user_email = serializers.CharField(
        source="user.email",
        read_only=True
    )

    class Meta:

        model = ActivityLog

        fields = "__all__"


class NotificationSerializer(
    serializers.ModelSerializer
):

    sender_email = serializers.CharField(
        source="sender.email",
        read_only=True
    )

    class Meta:

        model = Notification

        fields = "__all__"