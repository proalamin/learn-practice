# URL Routing Learning Path

## Step-by-Step from Basics to Advanced

---

## 📚 Table of Contents

1. [Learning Path Overview](#learning-path-overview)
2. [Step 1: URL Basics](#step-1-url-basics)
3. [Step 2: Django URL Patterns](#step-2-django-url-patterns)
4. [Step 3: Path Parameters](#step-3-path-parameters)
5. [Step 4: DRF Class-Based Views](#step-4-drf-class-based-views)
6. [Step 5: ViewSets](#step-5-viewsets)
7. [Step 6: Routers](#step-6-routers)
8. [Step 7: Nested Routers](#step-7-nested-routers)
9. [Step 8: Advanced Patterns](#step-8-advanced-patterns)
10. [Complete Real-World Example](#complete-real-world-example)

---

## 🎯 Learning Path Overview

```
Step 1: URL Basics
├─ What is a URL
├─ URL structure
└─ Query strings

Step 2: Django URL Patterns
├─ path() function
├─ Multiple patterns
└─ Include patterns

Step 3: Path Parameters
├─ Extracting IDs
├─ Type conversion
└─ Multiple parameters

Step 4: DRF Class-Based Views
├─ HTTP methods (GET, POST, etc)
├─ Request/Response
└─ Class methods

Step 5: ViewSets
├─ What ViewSets do
├─ ViewSet methods
└─ CRUD operations

Step 6: Routers (Simple)
├─ What routers do
├─ Auto-generating URLs
└─ Basename

Step 7: Nested Routers (Complex)
├─ Parent-child relationships
├─ Lookup parameters
└─ Multi-level nesting

Step 8: Advanced
├─ Custom actions
├─ Multiple nested levels
└─ Performance optimization
```

---

## Step 1: URL Basics

### What is a URL?

A URL (Uniform Resource Locator) is an address to access resources on the web.

```
http://localhost:8000/api/v1/products/
├─ http://        Protocol
├─ localhost:8000 Server address
├─ /api/v1/       Path (routes to the API)
└─ products/      Resource name
```

### URL Structure in DRF

```
http://localhost:8000/api/v1/products/1/reviews/5/
                      ├─── api/v1 ────┼─ products ─┼─ 1 ─┼─ reviews ─┼─ 5
                      │               │             │      │           │
                      Root            Base URL      Resource ID  Nested Resource ID
```

### Query Strings (Parameters)

```
http://localhost:8000/api/v1/products/?category=1&search=laptop
                                       ├─ ?category=1  (filter by category)
                                       ├─ &search=laptop (search term)
                                       └─ & (separator)
```

**No code needed yet!** Just understand the structure.

---

## Step 2: Django URL Patterns

### Basic URL Pattern

**File: `amin_shop_main/urls.py`**

```python
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),        # /admin/
    path('hello/', views.hello),            # /hello/
    path('products/', views.products),      # /products/
]
```

### How It Works

```
Request: GET http://localhost:8000/hello/
           ↓
Django checks: path('hello/', views.hello)
           ↓
Matches! Calls views.hello function
           ↓
Response returned
```

### Multiple Patterns

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root),
    path('products/', views.products),
    path('categories/', views.categories),
]
```

Each `path()` creates one URL endpoint.

### Include Pattern (Organizing URLs)

```python
# Main urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),  # Include from api/urls.py
]

# api/urls.py (separate file)
urlpatterns = [
    path('products/', views.products),
    path('categories/', views.categories),
]
```

**Result:**

- `/api/v1/products/` (combined path)
- `/api/v1/categories/`

---

## Step 3: Path Parameters

### Getting Specific Items by ID

**Without parameters (not flexible):**

```python
# ❌ Would need separate URL for each product
path('products/1/', views.product_1),
path('products/2/', views.product_2),
path('products/3/', views.product_3),
# ...impossible!
```

**With parameters (flexible):**

```python
# ✅ One URL pattern for all
path('products/<int:pk>/', views.product_detail),
```

### How Path Parameters Work

```
path('products/<int:pk>/', views.product_detail)
            ├─ <int:pk>
            ├─ < > = "this is a variable"
            ├─ int = "expect integer"
            └─ pk = "variable name"

Request: GET /products/5/
         ↓
Extracted: pk = 5
         ↓
Views.product_detail(request, pk=5)
         ↓
Can use pk in view
```

### Common Parameter Types

```python
path('products/<int:pk>/', ...)          # Integer: /products/5/
path('products/<str:name>/', ...)        # String: /products/laptop/
path('products/<slug:slug>/', ...)       # Slug: /products/gaming-laptop/
path('products/<uuid:id>/', ...)         # UUID: /products/abc-123-def/
```

### Multiple Parameters

```python
path('products/<int:product_id>/reviews/<int:review_id>/', views.review_detail)

Request: GET /products/5/reviews/10/
         ↓
Extracted: product_id=5, review_id=10
         ↓
views.review_detail(request, product_id=5, review_id=10)
```

**Practice Exercise:**
Create these URL patterns:

```python
path('users/<int:user_id>/orders/<int:order_id>/', ...)
path('categories/<str:category>/', ...)
```

---

## Step 4: DRF Class-Based Views

### Function-Based View (Old Way)

```python
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        return Response({"products": [...]})
    elif request.method == 'POST':
        return Response({"created": True})
```

### Class-Based View (Better)

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductList(APIView):
    def get(self, request):
        """Handle GET /products/"""
        return Response({"products": [...]})

    def post(self, request):
        """Handle POST /products/"""
        return Response({"created": True})

class ProductDetail(APIView):
    def get(self, request, pk):
        """Handle GET /products/{pk}/"""
        product = Product.objects.get(pk=pk)
        return Response(product_data)

    def put(self, request, pk):
        """Handle PUT /products/{pk}/"""
        return Response({"updated": True})

    def delete(self, request, pk):
        """Handle DELETE /products/{pk}/"""
        return Response(status=204)
```

### URL Patterns for Class-Based Views

```python
# urls.py
urlpatterns = [
    path('products/', ProductList.as_view()),           # /products/
    path('products/<int:pk>/', ProductDetail.as_view()), # /products/{id}/
]
```

### HTTP Method Mapping

```python
class ProductDetail(APIView):
    def get(self, request, pk):        # GET /products/{pk}/
        return Response(...)

    def post(self, request, pk):       # POST /products/{pk}/
        return Response(...)

    def put(self, request, pk):        # PUT /products/{pk}/
        return Response(...)

    def patch(self, request, pk):      # PATCH /products/{pk}/
        return Response(...)

    def delete(self, request, pk):     # DELETE /products/{pk}/
        return Response(...)
```

**Key Concept:** One class handles multiple HTTP methods!

---

## Step 5: ViewSets

### What is a ViewSet?

A ViewSet combines multiple related views into ONE class. Instead of:

```python
# ❌ Two classes
class ProductList(APIView):
    def get(self, request): ...
    def post(self, request): ...

class ProductDetail(APIView):
    def get(self, request, pk): ...
    def put(self, request, pk): ...
    def delete(self, request, pk): ...

# Need TWO URL patterns
urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]
```

You can use ONE ViewSet:

```python
# ✅ One class
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # Methods are called automatically:
    # list()              GET /products/
    # create()            POST /products/
    # retrieve()          GET /products/{pk}/
    # update()            PUT /products/{pk}/
    # partial_update()    PATCH /products/{pk}/
    # destroy()           DELETE /products/{pk}/

# Only ONE URL pattern (router generates the rest!)
```

### ViewSet Methods

When a ViewSet is registered, it has these methods:

```python
class ProductViewSet(ModelViewSet):

    # Automatically implemented by ModelViewSet:

    def list(self, request):
        """GET /products/ - List all products"""
        pass

    def create(self, request):
        """POST /products/ - Create new product"""
        pass

    def retrieve(self, request, pk=None):
        """GET /products/{pk}/ - Get one product"""
        pass

    def update(self, request, pk=None):
        """PUT /products/{pk}/ - Full update"""
        pass

    def partial_update(self, request, pk=None):
        """PATCH /products/{pk}/ - Partial update"""
        pass

    def destroy(self, request, pk=None):
        """DELETE /products/{pk}/ - Delete"""
        pass
```

### ViewSet Types

**1. ModelViewSet** - Full CRUD

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
# Provides: list, create, retrieve, update, partial_update, destroy
```

**2. ReadOnlyModelViewSet** - Only list & retrieve

```python
class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# Provides: list, retrieve (no create/update/delete)
```

---

## Step 6: Routers

### What is a Router?

A **Router** auto-generates URL patterns from ViewSets.

**Without router (manual):**

```python
urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
```

**With router (automatic):**

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls  # That's it! All URLs generated!
```

### How Router Works

```
router.register('products', ProductViewSet)
           ↓
Router inspects ProductViewSet
           ↓
Sees: list, create, retrieve, update, destroy methods
           ↓
Auto-generates:
    GET    /products/          → list()
    POST   /products/          → create()
    GET    /products/{pk}/     → retrieve()
    PUT    /products/{pk}/     → update()
    PATCH  /products/{pk}/     → partial_update()
    DELETE /products/{pk}/     → destroy()
```

### Complete Router Example

**File: `api/urls.py`**

```python
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, CategoryViewSet

# Create router
router = DefaultRouter()

# Register ViewSets
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')

# Use router URLs
urlpatterns = router.urls

# This generates:
# GET    /products/
# POST   /products/
# GET    /products/{id}/
# PUT    /products/{id}/
# PATCH  /products/{id}/
# DELETE /products/{id}/
# GET    /categories/
# GET    /categories/{id}/
# etc.
```

### Router Types

**DefaultRouter** - Shows API root

```python
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# Includes GET / (shows all endpoints)
```

**SimpleRouter** - Just routes

```python
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
# No API root view
```

**basename Parameter**

```python
router.register('products', ProductViewSet, basename='products')
                                            ├─ 'products'
                                            └─ Used for naming
                                               'products-list'
                                               'products-detail'
```

---

## Step 7: Nested Routers

### The Problem

You want URLs like:

```
/products/1/reviews/      (reviews for product 1)
/products/1/reviews/5/    (review 5 of product 1)
/products/2/reviews/      (reviews for product 2)
```

**Can't do this with simple routers!**

### Solution: Nested Routers

```python
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from product.views import ProductViewSet, ReviewViewSet

# Main router
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

# Nested router (depends on products)
reviews_router = routers.NestedDefaultRouter(
    router,           # Parent router
    'products',       # Parent resource name
    lookup='product'  # URL param will be 'product_pk'
)
reviews_router.register('reviews', ReviewViewSet, basename='product-review')

# Include both
urlpatterns = [
    path('', include(router.urls)),
    path('', include(reviews_router.urls)),
]
```

### What Gets Generated

```
Parent URLs:
GET    /products/
POST   /products/
GET    /products/{id}/
PUT    /products/{id}/
DELETE /products/{id}/

Nested URLs:
GET    /products/{product_pk}/reviews/
POST   /products/{product_pk}/reviews/
GET    /products/{product_pk}/reviews/{id}/
PUT    /products/{product_pk}/reviews/{id}/
DELETE /products/{product_pk}/reviews/{id}/
```

### Understanding `lookup='product'`

```python
lookup='product'
    ↓
URL parameter name: product_pk  (lookup + '_pk')
    ↓
In ReviewViewSet, access via: self.kwargs['product_pk']
```

### Filtering Nested Resources

When accessing `/products/1/reviews/`, you need to filter:

```python
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """Only reviews for the parent product"""
        product_pk = self.kwargs['product_pk']
        return Review.objects.filter(product_id=product_pk)
```

### Real Example: Products & Reviews

**models.py:**

```python
class Product(models.Model):
    name = models.CharField(max_length=100)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
```

**views.py:**

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_pk = self.kwargs['product_pk']
        return Review.objects.filter(product_id=product_pk)
```

**urls.py:**

```python
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

reviews_router = routers.NestedDefaultRouter(
    router,
    'products',
    lookup='product'
)
reviews_router.register('reviews', ReviewViewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(reviews_router.urls)),
]
```

**Usage:**

```
GET /products/          → list all products
GET /products/1/        → get product 1
GET /products/1/reviews/    → reviews for product 1
GET /products/1/reviews/5/  → review 5 of product 1
POST /products/1/reviews/   → add review to product 1
```

---

## Step 8: Advanced Patterns

### Pattern 1: Multi-Level Nesting

```
/users/1/orders/
/users/1/orders/5/items/
/users/1/orders/5/items/10/
```

**Setup:**

```python
# Level 1: Users
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

# Level 2: Orders under Users
orders_router = NestedDefaultRouter(router, 'users', lookup='user')
orders_router.register('orders', OrderViewSet, basename='user-order')

# Level 3: Items under Orders
items_router = NestedDefaultRouter(orders_router, 'orders', lookup='order')
items_router.register('items', OrderItemViewSet, basename='order-item')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(orders_router.urls)),
    path('', include(items_router.urls)),
]
```

**ViewSet filtering:**

```python
class OrderItemViewSet(ModelViewSet):
    def get_queryset(self):
        user_pk = self.kwargs['user_pk']
        order_pk = self.kwargs['order_pk']
        return OrderItem.objects.filter(
            order__user_id=user_pk,
            order_id=order_pk
        )
```

### Pattern 2: Custom Actions

```python
class ProductViewSet(ModelViewSet):
    @action(detail=False, methods=['get'])
    def popular(self, request):
        """GET /products/popular/"""
        popular = Product.objects.filter(rating__gte=4)
        serializer = self.get_serializer(popular, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_featured(self, request, pk=None):
        """POST /products/{pk}/set_featured/"""
        product = self.get_object()
        product.is_featured = True
        product.save()
        return Response({"status": "featured"})
```

**Generated URLs:**

```
GET /products/popular/
POST /products/1/set_featured/
```

### Pattern 3: Query Parameters & Filtering

```
GET /products/?category=1&search=laptop&ordering=-price&page=1
```

**ViewSet:**

```python
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'stock']
```

---

## Complete Real-World Example

### Your Project Structure

Let me use your actual project: **amin_shop_drf**

### Step 1: Models

```python
# product/models.py
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

# order/models.py
class Cart(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
```

### Step 2: ViewSets

```python
# product/views.py
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['price']

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_pk = self.kwargs['product_pk']
        return Review.objects.filter(product_id=product_pk)

# order/views.py
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

class CartItemViewSet(ModelViewSet):
    def get_queryset(self):
        cart_pk = self.kwargs['cart_pk']
        return CartItem.objects.filter(cart_id=cart_pk)
```

### Step 3: Routers

```python
# api/urls.py
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers as nested_routers
from product.views import ProductViewSet, ReviewViewSet, CategoryViewSet
from order.views import CartViewSet, CartItemViewSet

# Main router
router = nested_routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('carts', CartViewSet, basename='carts')

# Nested routers
products_router = nested_routers.NestedDefaultRouter(
    router,
    'products',
    lookup='product'
)
products_router.register('reviews', ReviewViewSet, basename='product-review')

carts_router = nested_routers.NestedDefaultRouter(
    router,
    'carts',
    lookup='cart'
)
carts_router.register('items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    path('', include(carts_router.urls)),
]
```

### Step 4: Generated URLs

```
PRODUCTS:
GET    /products/
POST   /products/
GET    /products/{id}/
PUT    /products/{id}/
PATCH  /products/{id}/
DELETE /products/{id}/

REVIEWS (Nested):
GET    /products/{product_pk}/reviews/
POST   /products/{product_pk}/reviews/
GET    /products/{product_pk}/reviews/{id}/
PUT    /products/{product_pk}/reviews/{id}/
DELETE /products/{product_pk}/reviews/{id}/

CARTS:
POST   /carts/
GET    /carts/{id}/
DELETE /carts/{id}/

CART ITEMS (Nested):
GET    /carts/{cart_pk}/items/
POST   /carts/{cart_pk}/items/
GET    /carts/{cart_pk}/items/{id}/
PATCH  /carts/{cart_pk}/items/{id}/
DELETE /carts/{cart_pk}/items/{id}/
```

---

## 🎯 Practice Exercises

### Exercise 1: Basic URL Pattern

Create a URL pattern that matches:

- `/blog/` → list posts
- `/blog/5/` → get post 5

```python
# Solution:
path('blog/', views.blog_list),
path('blog/<int:pk>/', views.blog_detail),
```

### Exercise 2: ViewSet

Create a ViewSet for a `Book` model with:

- List books
- Create book
- Get one book
- Update book
- Delete book

```python
# Solution:
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

### Exercise 3: Nested Router

Create nested URLs for:

- `/books/` - list books
- `/books/1/chapters/` - chapters of book 1
- `/books/1/chapters/3/` - chapter 3 of book 1

```python
# Solution:
router = DefaultRouter()
router.register('books', BookViewSet, basename='books')

chapters_router = NestedDefaultRouter(router, 'books', lookup='book')
chapters_router.register('chapters', ChapterViewSet, basename='book-chapter')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(chapters_router.urls)),
]
```

---

## 📊 URL Flow Diagram (Complete)

```
REQUEST
  ↓
┌─────────────────────────────────────┐
│ Step 1: URL MATCHING                │
│ Django searches: path(), include()  │
│                                     │
│ GET /api/v1/products/1/reviews/5/   │
│ Matches: NestedDefaultRouter        │
│ Route: products/{product_pk}/reviews│
│ Params: product_pk=1, pk=5          │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Step 2: VIEWSET SELECTION           │
│ Router: Which ViewSet handles this? │
│ Answer: ReviewViewSet               │
│ Method: GET + detail = retrieve()   │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Step 3: FILTER QUERYSET             │
│ get_queryset()                      │
│ Filter: product_id = 1              │
│ Get: Review with id = 5             │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Step 4: SERIALIZE                   │
│ Convert Review object → JSON        │
└─────────────────────────────────────┘
  ↓
RESPONSE (JSON)
```

---

## 🎓 Summary Table

| Concept       | What                | Why               | Example                  |
| ------------- | ------------------- | ----------------- | ------------------------ |
| URL Pattern   | Maps URL to view    | Route requests    | `path('products/', ...)` |
| Parameter     | Extract ID from URL | Get specific item | `<int:pk>`               |
| ViewSet       | Combines CRUD       | Less code         | `ModelViewSet`           |
| Router        | Auto-generates URLs | DRY principle     | `router.register()`      |
| Nested Router | Child resource      | Logical hierarchy | `products → reviews`     |

---

## 🚀 Next Steps

1. **Read** ROUTING_GUIDE.md for complete details
2. **Test** endpoints from API_EXAMPLES.md
3. **Create** a simple API with:
   - Products endpoint
   - Reviews nested under products
   - Cart endpoint
4. **Experiment** - Modify ViewSets and see URL changes

---

## ❓ Common Questions

**Q: Why use routers instead of writing paths manually?**
A: Routers auto-generate 6+ URLs from one ViewSet. Much less code!

**Q: What's the difference between `pk` and `product_pk`?**
A: `pk` is for the current resource. `product_pk` is for the parent resource in nested routes.

**Q: Can I have 3 levels of nesting?**
A: Yes! `users/orders/items` - but can get complex. Use wisely.

**Q: How do I filter nested resources?**
A: Override `get_queryset()` and use `self.kwargs['parent_pk']`

**Q: What if I need custom logic in a route?**
A: Use `@action` decorator for custom endpoints

---

**Now you understand routing! Start with Step 1 and work through to Step 8.** 🚀
