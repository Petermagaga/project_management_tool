from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    created_by_email=serializers.CharField(source="created_by.email", read_only=True)
    class Meta:
        model=Project
        fields="__all__"
        read_only_fields=( "created_by",)

        