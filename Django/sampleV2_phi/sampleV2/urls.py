
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('insert_data/', views.insert_data, name='insertData'),
    path('views/', views.views_data, name='views'),
    path('edit_data/<int:id>', views.edit_data, name='edit_data'),
    path('update_data/', views.update, name='update_data'),
    path('delate_single_user/<int:id>', views.delate_single_user, name='delate_single_user'),
    path('verify/<int:id>/', views.verify_email, name='verify_email'),
    path('verify_otp/<int:user_id>/', views.verify_otp, name='verify_otp'),

]
