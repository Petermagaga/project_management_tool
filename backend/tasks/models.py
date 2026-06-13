from django.db import models
from django.conf import settings

from projects.models import Project
from boards.models import Board
class Task(models.Model):
    PRIORITY_CHOICES=[

        ("LOW","Low"),
        ("MEDIUM","Medium"),
        ("HIGH","High"),
        ("URGENT","Urgent"),
    ]
    board=models.ForeignKey(Board,on_delete=models.CASCADE,related_name="tasks")
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks")
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    priority=models.CharField(choices=PRIORITY_CHOICES,default="MEDIUM")
    assignee=models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,
        null=True,blank=True,related_name="assigned_tasks"
    )
    reporter=models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True, related_name="reporter_tasks"
    )

    due_date=models.DateField(
        null=True,blank=True
    )
    estimated_hours=models.PositiveIntegerField(default=0)
    labels=models.JSONField(default=list,blank=True)
    position=models.PositiveIntegerField( default=0)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["position"]
    
    def __str__(self):
        return self.title 