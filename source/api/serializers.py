from rest_framework import serializers
from webapp.models import Project, Issue, Status, Type


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'started_at', 'finished_at', 'is_deleted', 'user']
        read_only_fields = ['id']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'name']
        read_only_fields = ['id', 'name']


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ['id', 'name']
        read_only_fields = ['id']


class IssueSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'summary', 'description', 'is_deleted', 'project', 'status', 'type', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
