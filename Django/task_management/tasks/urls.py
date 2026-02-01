from django.urls import path
from tasks.views import show_task, new_task, task_id

urlpatterns =[
    path('show-task/', show_task),
    path('new-task/', new_task),
    path('new-task/<int:id>/', task_id)
]