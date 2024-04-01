from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task


class TaskList(APIView):
    def get(self, request, format=None):
        task = Task.objects.all()
        serializers = TaskSerializer(task, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
