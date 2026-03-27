from django.urls import path
from product import views

urlpatterns = [
    path('', views.view_products, name='product-all'),
    path('<int:id>/', views.view_specific_products, name='product-list')
]
