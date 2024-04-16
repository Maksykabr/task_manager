from django.urls import path, include
from .views import TaskList, AddTask, HomePage, GetCompletedTasks, GetAllTasks, GetEditPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('task_list', TaskList.as_view(), name='active_task'),
    path('task_list/<int:pk>', TaskList.as_view(), name='complete_task'),
    path('add_task', AddTask.as_view(), name='add_task'),
    path('completed_task', GetCompletedTasks.as_view(), name='completed_tasks'),
    path('completed_task/<int:pk>', GetCompletedTasks.as_view(), name='incomplete_task'),
    path('all_tasks', GetAllTasks.as_view(), name='all_tasks'),
    path('edit_page/<int:pk>', GetEditPage.as_view(), name='edit_task'),
]