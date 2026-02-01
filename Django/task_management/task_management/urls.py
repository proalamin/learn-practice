from django.contrib import admin
from django.urls import path, include
from tasks.views import home
from users.views import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('users/', user),
    path('', include("tasks.urls"))
]