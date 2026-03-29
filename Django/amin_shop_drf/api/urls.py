from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from product.views import ProductViewSet, CategoryViewSets

# urlpatterns = [
#     path('products/', include('product.product_urls')),
#     path('categories/', include('product.categories_urls'))
    
# ] 

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSets)

# urlpatterns = router.urls


# router and others url want ot use
urlpatterns=[
    path('', include(router.urls)),
    # have more paths
    #path ('simple/', .....)
]

