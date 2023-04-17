from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Issue, Project
from api.serializers import IssueSerializer, ProjectSerializer


class IssueDetailView(APIView):

    def get(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=kwargs['pk'])
        serializer = IssueSerializer(issue)
        return Response(serializer.data)


class IssueUpdateView(APIView):

    def get(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=kwargs['pk'])
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

    def put(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(issue, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDeleteView(APIView):

    def get(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=kwargs['pk'])
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        issue = Issue.objects.get(pk=pk)
        issue.delete()
        return Response(data={"id": issue.id})


class ProjectDetailView(APIView):

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['pk'])
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class ProjectUpdateView(APIView):

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['pk'])
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDeleteView(APIView):

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['pk'])
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(data={"id": project.id})
