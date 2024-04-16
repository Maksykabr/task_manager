from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import TaskSerializer
from .models import Task
from datetime import datetime, date


class TaskList(APIView):
    def get(self, request, pk=None, format=None):
        current_date = date.today()
        tasks = Task.objects.filter(selected_data=current_date, completed=False)
        serializers = TaskSerializer(tasks, many=True)
        context = {
            'active': 'Active_tasks',
            'tasks': serializers.data,

        }
        return render(request, 'task_manager/task_list.html', context=context,)

    def post(self, request, pk=None):
        if request.method == 'POST':
            if pk is None:
                return HttpResponseBadRequest("Task ID is required.")
            task = Task.objects.get(pk=pk)
            task.completed = True  # Змінюємо значення на True
            task.save()
            return redirect('active_task')


class AddTask(APIView):
    def get(self, reuests, format=None):
        context = {
            'active': 'Create_task',
        }
        return render(reuests, 'task_manager/add_task.html', context=context)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return redirect('active_task')
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCompletedTasks(APIView):
    def get(self,request, pk=None, format=None):
        current_date = date.today()
        tasks = Task.objects.filter(selected_data=current_date, completed=True)
        serializers = TaskSerializer(tasks, many=True)
        context = {
            'active': 'Completed_tasks',
            'tasks': serializers.data,

        }
        return render(request, 'task_manager/completed_tasks.html', context=context)

    def post(self, request, pk=None, format=None):
        if request.method == 'POST':
            if pk is None:
                return HttpResponseBadRequest("Task ID is required.")
            task = Task.objects.get(pk=pk)
            task.completed = False  # Змінюємо значення на True
            task.save()
            return redirect('completed_tasks')

class GetAllTasks(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializers = TaskSerializer(tasks, many=True)
        context = {
            'active': 'All_tasks',
            'tasks': serializers.data,

        }
        return render(request, 'task_manager/all_tasks.html', context=context)


class GetEditPage(APIView):
    def get(self, request, pk=None, format=None):
        task = Task.objects.get(pk=pk)
        serializers = TaskSerializer(task, many=False)
        context = {
            'active': 'Edit task',
            'task': serializers.data
        }
        return render(request, 'task_manager/edit_page.html', context=context)

    def post(self, request, pk=None, format=None):
        if request.method == 'POST':
            if pk is None:
                return HttpResponseBadRequest("Task ID is required.")
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('active_task')

class HomePage(APIView):
    def get(self, request):

        return render(request, 'task_manager/home.html')


