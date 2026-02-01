from django.urls import path
from tasks.views import show_task, new_task

urlpatterns =[
    path('show-task/', show_task),
    path('new-task/', new_task),
]