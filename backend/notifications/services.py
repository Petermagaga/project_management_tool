from .models import ActivityLog,Notification


from asgiref.sync import (
    async_to_sync
)

from channels.layers import (
    get_channel_layer
)

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

    notification = Notification.objects.create(

        recipient=recipient,

        sender=sender,

        notification_type=notification_type,

        message=message
    )

    channel_layer = (
        get_channel_layer()
    )

    async_to_sync(
        channel_layer.group_send
    )(

        f"user_{recipient.id}",

        {

            "type":
                "send_notification",

            "message":
                message
        }
    )

    return notification