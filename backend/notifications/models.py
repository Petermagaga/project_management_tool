from django.db import models
from django.conf import settings

from projects.models import Project


class ActivityLog(models.Model):

    ACTION_TYPES = [

        ("TASK_CREATED", "Task Created"),

        ("TASK_UPDATED", "Task Updated"),

        ("TASK_MOVED", "Task Moved"),

        ("TASK_DELETED", "Task Deleted"),

        ("COMMENT_CREATED", "Comment Created"),

        ("PROJECT_CREATED", "Project Created"),

        ("PROJECT_UPDATED", "Project Updated"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="activity_logs"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    action_type = models.CharField(
        max_length=50,
        choices=ACTION_TYPES
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-created_at"]

    def __str__(self):

        return self.message[:50]
    
class Notification(models.Model):

    NOTIFICATION_TYPES = [

        ("TASK_ASSIGNED", "Task Assigned"),

        ("TASK_COMMENT", "Task Comment"),

        ("TASK_DUE", "Task Due"),

        ("MENTION", "Mention"),

        ("PROJECT_INVITE", "Project Invite"),
    ]

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_notifications"
    )

    notification_type = models.CharField(
        max_length=50,
        choices=NOTIFICATION_TYPES
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-created_at"] 
        indexes= [
            models.Index(
                fields=[
                    "recipient",
                    "is_read"
                ]
            )
        ]


    def __str__(self):

        return self.message[:50]

