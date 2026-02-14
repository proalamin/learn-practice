
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('api.urls')),
    # path('customers/', include('student.urls'))
]
