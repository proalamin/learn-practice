from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet, CategoryViewSets

# urlpatterns = [
#     path('products/', include('product.product_urls')),
#     path('categories/', include('product.categories_urls'))
    
# ] 

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSets)

urlpatterns = router.urls

