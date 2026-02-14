
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import customerListCreateView, customerDetailView

urlpatterns = [
    # path('demo/', views.demo),
    # path('customers/', include('student.urls'))
    
    path('customers/', customerListCreateView.as_view()),
    path('customers/<int:pk>/', customerDetailView.as_view()),


]
