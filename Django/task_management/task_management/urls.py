from django.contrib import admin
from django.urls import path, include
# from tasks.views import manager_dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', manager_dashboard),
    path('tasks/', include("tasks.urls"))
]