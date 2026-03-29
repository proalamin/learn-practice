from django.urls import path
from product import views

urlpatterns = [
    # path('', views.view_products, name='product-all'), # function based views
    # path('', views.ViewProduct.as_view(), name='product-all'), # class based views
    path('', views.ProductList.as_view(), name='product-all'), # generic views 
    
    # path('<int:id>/', views.view_specific_products, name='product-list'), # function based views
    # path('<int:id>/', views.ViewSpecificProduct.as_view(), name='product-list'), # class based views
    path('<int:id>/', views.ProductDetails.as_view(), name='product-list'), # generic views 
    
]
