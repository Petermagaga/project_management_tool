from .models import WorkspaceMember


def get_user_role(user,workspace):


    membership=WorkspaceMember.objects.filter(workspace=workspace,user=user).first()

    if membership:
        return membership.role
    
    return None