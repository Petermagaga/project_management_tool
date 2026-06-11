from django.db import models

from projects.models import Project

class Board(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="boards")
    name=models.CharField(max_length=255)
    position=models.PositiveBigIntegerField(default=0)

    create_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=["position"]

    def __str__(self):
        return f"{self.project.name} - {self.name}"