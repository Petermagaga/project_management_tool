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