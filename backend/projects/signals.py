from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project
from boards.models import Board

@receiver(post_save,sender=Project)
def create_default_boards(sender,instance,created,**kwargs):

    if created:
        default_boards =[
            "Backlog",
            "To do",
            "In Progress",
            "Review",
            "Done"
        ]

        for index, name in enumerate(default_boards):
            Board.objects.create(project=instance,
                                 name=name,
                                 position=index)