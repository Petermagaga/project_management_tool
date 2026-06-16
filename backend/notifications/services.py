from .models import ActivityLog,Notification



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



def create_notification(

    recipient,

    sender,

    notification_type,

    message

):

    Notification.objects.create(

        recipient=recipient,

        sender=sender,

        notification_type=notification_type,

        message=message
    )