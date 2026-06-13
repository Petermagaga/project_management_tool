from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "task",
        "user",
        "created_at",
    )

    search_fields = (
        "content",
        "user__email",
        "task__title",
    )