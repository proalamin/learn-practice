from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from product.views import ProductViewSet, CategoryViewSets, ReviewViewSet
from rest_framework_nested import routers


# urlpatterns = [
#     path('products/', include('product.product_urls')),
#     path('categories/', include('product.categories_urls'))
    
# ] 

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSets)

# urlpatterns = router.urls

product_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
product_router.register('reviews', ReviewViewSet, basename= 'product-review')

urlpatterns=[
    path('', include(router.urls)),
    path('', include(product_router.urls))
]

