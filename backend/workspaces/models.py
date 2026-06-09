from django.db import models
from django.conf import settings

class Workspace(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                            related_name="owned_workspaces")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WorkspaceMember(models.Model):
    ROLES_choices=[
        ("OWNER","Owner"),
        ("ADMIN",'admin'),
        ("MEMBER",'member'),
        ("VIEWER","viewer"),
    ]

    workspace=models.ForeignKey(
        Workspace,on_delete=models.CASCADE,
        related_name="members"
    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    role=models.CharField(choices=ROLES_choices,default="MEMBER")

    joined_at=models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        unique_together=(
            "workspace",
            "user"
        )

    def __str__(self):
        return f"{self.user.email} -{self.role}"

