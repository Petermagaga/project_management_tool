from rest_framework.permissions import BasePermission

from workspaces.permissions import (get_user_role)

class CanManageProject(BasePermission):
    def has_object_permission(self,request,view,obj):
        role=get_user_role(request.user,obj.workspace)

        return role in ["owner","admin"]
    
    