from .models import ActivityLog



def create_activity_log(

    project,

    user,

    action_type,

    message

):

    ActivityLog.objects.create(

        project=project,

        user=user,

        action_type=action_type,

        message=message
    )