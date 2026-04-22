# ViewSets, Mixins & Generics Explained

## Deep Dive into Django REST Framework Views

---

## 📌 Table of Contents

1. [Views Evolution](#views-evolution)
2. [Function-Based Views (FBV)](#function-based-views-fbv)
3. [Class-Based Views (CBV)](#class-based-views-cbv)
4. [Generic Views](#generic-views)
5. [Mixins](#mixins)
6. [ViewSets](#viewsets)
7. [Router Auto-Generation](#router-auto-generation)
8. [Complete Examples](#complete-examples)

---

## 📚 Views Evolution

DRF provides multiple ways to write views, each more powerful than the last:

```
1. Function-Based Views
   ↓ (More code, less features)

2. Class-Based Views (APIView)
   ↓ (Still manual CRUD handling)

3. Generic Views (Generics)
   ↓ (Common patterns automated)

4. ViewSets with Routers
   ↑ (Least code, most features)
```

---

## 🔧 Function-Based Views (FBV)

### Simplest but Most Verbose

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

**Problems:**

- Lots of repetitive code
- Manual error handling
- Manual pagination
- Manual filtering
- Manual authentication

---

## 👁️ Class-Based Views (CBV)

### Better Organization

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

**Better, but:**

- Still repetitive for CRUD
- Still manual pagination/filtering
- Still manual error handling

---

## 📦 Generic Views

### Common Patterns Automated

```python
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
```

**Much cleaner!**

### Common Generic Classes

```
ListAPIView
├─ List: GET /products/
RetrieveAPIView
├─ Retrieve: GET /products/{id}/

CreateAPIView
├─ Create: POST /products/

UpdateAPIView
├─ Update: PUT /products/{id}/

DestroyAPIView
├─ Delete: DELETE /products/{id}/

ListCreateAPIView
├─ List: GET /products/
├─ Create: POST /products/

RetrieveUpdateAPIView
├─ Retrieve: GET /products/{id}/
├─ Update: PUT /products/{id}/

RetrieveUpdateDestroyAPIView
├─ Retrieve: GET /products/{id}/
├─ Update: PUT /products/{id}/
├─ Delete: DELETE /products/{id}/

RetrieveDestroyAPIView
├─ Retrieve: GET /products/{id}/
├─ Delete: DELETE /products/{id}/
```

---

## 🧩 Mixins

### Build-Your-Own Generic Views

Mixins provide individual actions:

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class CreateModelMixin:
    """Add create() method"""

class ListModelMixin:
    """Add list() method"""

class RetrieveModelMixin:
    """Add retrieve() method"""

class UpdateModelMixin:
    """Add update() and partial_update() methods"""

class DestroyModelMixin:
    """Add destroy() method"""
```

### Combine Mixins to Build Custom ViewSet

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Cart can be created, retrieved, and destroyed (not updated)
class CartViewSet(
    CreateModelMixin,      # POST /carts/
    RetrieveModelMixin,    # GET /carts/{id}/
    DestroyModelMixin,     # DELETE /carts/{id}/
    GenericViewSet         # Base ViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

# This allows:
# POST   /carts/              (create)
# GET    /carts/{id}/         (retrieve)
# DELETE /carts/{id}/         (destroy)
#
# But NOT:
# GET    /carts/              (list) - no ListModelMixin
# PUT    /carts/{id}/         (update) - no UpdateModelMixin
# PATCH  /carts/{id}/         (partial_update) - no UpdateModelMixin
```

### Mixin Inheritance Order Matters

```python
# Wrong order (won't work as expected)
class BadViewSet(
    GenericViewSet,        # Base first
    CreateModelMixin,
    ListModelMixin
):
    pass

# Correct order (specific mixins first)
class GoodViewSet(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet         # Base last
):
    pass
```

---

## 🎯 ViewSets

### What ViewSets Do

A **ViewSet** combines related views into a single class.

**ViewSet Types:**

1. **ModelViewSet** - Full CRUD

   ```python
   class ProductViewSet(ModelViewSet):
       queryset = Product.objects.all()
       serializer_class = ProductSerializers

   # Provides all 6 operations:
   # GET    /products/              list()
   # POST   /products/              create()
   # GET    /products/{id}/         retrieve()
   # PUT    /products/{id}/         update()
   # PATCH  /products/{id}/         partial_update()
   # DELETE /products/{id}/         destroy()
   ```

2. **ReadOnlyModelViewSet** - Only GET

   ```python
   class CategoryViewSet(ReadOnlyModelViewSet):
       queryset = Category.objects.all()
       serializer_class = CategorySerializer

   # Provides only read operations:
   # GET    /categories/            list()
   # GET    /categories/{id}/       retrieve()
   ```

3. **Custom ViewSet** - Mix and Match

   ```python
   class CartViewSet(
       CreateModelMixin,
       RetrieveModelMixin,
       DestroyModelMixin,
       GenericViewSet
   ):
       queryset = Cart.objects.all()
       serializer_class = CartSerializers

   # Provides:
   # POST   /carts/                 create()
   # GET    /carts/{id}/            retrieve()
   # DELETE /carts/{id}/            destroy()
   ```

### ViewSet Methods

ViewSets automatically map HTTP methods to ViewSet methods:

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # Automatically called based on HTTP method and URL
    def list(self, request, *args, **kwargs):
        """GET /products/ - List all"""
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """POST /products/ - Create new"""
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """GET /products/{pk}/ - Get one"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """PUT /products/{pk}/ - Full update"""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """PATCH /products/{pk}/ - Partial update"""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """DELETE /products/{pk}/ - Delete"""
        return super().destroy(request, *args, **kwargs)
```

### Override ViewSet Methods

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_queryset(self):
        """Custom filtering"""
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category_id=category)
        return queryset

    def get_serializer_class(self):
        """Different serializer for different methods"""
        if self.request.method == 'POST':
            return ProductCreateSerializer  # For creating
        return ProductSerializers  # For retrieving

    def perform_create(self, serializer):
        """Custom logic before save"""
        print(f"Creating product: {serializer.validated_data}")
        serializer.save()

    def perform_update(self, serializer):
        """Custom logic during update"""
        print(f"Updating product: {serializer.validated_data}")
        serializer.save()

    def perform_destroy(self, instance):
        """Custom logic before delete"""
        print(f"Deleting product: {instance.name}")
        instance.delete()
```

---

## 🔄 Router Auto-Generation

### How Routers Work

When you register a ViewSet with a router:

```python
router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
```

The router automatically inspects the ViewSet and generates URLs:

```
┌─────────────────────────────────────────────┐
│ ViewSet methods available?                  │
├─────────────────────────────────────────────┤
│ list()              → GET    /products/     │
│ create()            → POST   /products/     │
│ retrieve()          → GET    /products/{pk}/│
│ update()            → PUT    /products/{pk}/│
│ partial_update()    → PATCH  /products/{pk}/│
│ destroy()           → DELETE /products/{pk}/│
└─────────────────────────────────────────────┘
```

### Different Routers

**1. DefaultRouter**

```python
router = DefaultRouter()
# Includes default API root view
# Shows all endpoints at /api/
```

**2. SimpleRouter**

```python
router = SimpleRouter()
# Just the routes, no API root view
```

**3. NestedRouter (drf-nested-routers)**

```python
router = routers.DefaultRouter()
router.register('products', ProductViewSet)

# Nested under products
nested_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
nested_router.register('reviews', ReviewViewSet, basename='product-review')

# Generates:
# GET /products/{product_pk}/reviews/
# POST /products/{product_pk}/reviews/
# GET /products/{product_pk}/reviews/{review_pk}/
# etc.
```

---

## 📝 Complete Examples

### Example 1: Complete Product ViewSet

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class ProductViewSet(ModelViewSet):
    """
    Full CRUD endpoint for products.

    Supports:
    - Filtering: ?category=1
    - Search: ?search=laptop
    - Ordering: ?ordering=-price
    - Pagination: ?page=1
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'stock']
    pagination_class = DefaultPagination

    def get_queryset(self):
        """Optimize queries with select_related"""
        return Product.objects.select_related('category')

    def get_serializer_context(self):
        """Pass additional context to serializer"""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        """Add user to product creation"""
        serializer.save()

    @action(detail=True, methods=['post'])
    def set_discount(self, request, pk=None):
        """Custom action: POST /products/{pk}/set_discount/"""
        product = self.get_object()
        discount = request.data.get('discount')

        if not discount or discount < 0:
            return Response(
                {'error': 'Invalid discount'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Apply discount
        product.discount = discount
        product.save()

        return Response(
            {'message': 'Discount set'},
            status=status.HTTP_200_OK
        )
```

### Example 2: Restricted Cart ViewSet

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class CartViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    """
    Shopping cart endpoint.

    Supports:
    - Create: POST /carts/
    - Retrieve: GET /carts/{id}/
    - Delete: DELETE /carts/{id}/

    Does NOT support:
    - List: GET /carts/ (no ListModelMixin)
    - Update: PUT/PATCH (no UpdateModelMixin)
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

    def get_serializer_context(self):
        """Pass cart_id to nested items"""
        context = super().get_serializer_context()
        context['cart_id'] = self.kwargs.get('pk')
        return context
```

### Example 3: CartItem with Context-Aware Serializers

```python
class CartItemViewSet(ModelViewSet):
    """Cart items with dynamic serializer selection"""

    def get_serializer_class(self):
        """Select serializer based on HTTP method"""
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        """Pass cart_pk to serializer for validation"""
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        """Filter items for specific cart"""
        cart_pk = self.kwargs.get('cart_pk')
        return CartItem.objects.filter(cart_id=cart_pk)
```

---

## 🎨 Design Patterns

### Pattern 1: Different Serializers per Method

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer  # Minimal fields
        elif self.request.method in ['PUT', 'PATCH']:
            return ProductUpdateSerializer  # Different rules
        return ProductDetailSerializer  # Full details
```

### Pattern 2: Custom Actions

```python
class ProductViewSet(ModelViewSet):
    @action(detail=False, methods=['get'])
    def popular(self, request):
        """GET /products/popular/ - Top products"""
        popular_products = Product.objects.filter(
            reviews__gt=100
        ).distinct()
        serializer = self.get_serializer(popular_products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        """POST /products/{pk}/favorite/ - Mark as favorite"""
        product = self.get_object()
        # Add to user favorites
        return Response({'status': 'product marked as favorite'})
```

### Pattern 3: Filtered QuerySet

```python
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers

    def get_queryset(self):
        """Filter by user's permissions"""
        if self.request.user.is_staff:
            return Product.objects.all()
        else:
            return Product.objects.filter(is_public=True)
```

---

## ✅ Summary

| Type     | Code  | Features                   |
| -------- | ----- | -------------------------- |
| FBV      | Most  | Manual, verbose            |
| CBV      | More  | Organized, still manual    |
| Generics | Less  | Automated CRUD             |
| Mixins   | Less  | Custom combinations        |
| ViewSets | Least | Routers auto-generate URLs |

**Best Practice:** Use **ViewSets with Routers** for most cases! 🚀

They provide:

- Minimal code
- Automatic URL generation
- Built-in pagination, filtering, search
- Consistent API design
- Easy to maintain and extend
