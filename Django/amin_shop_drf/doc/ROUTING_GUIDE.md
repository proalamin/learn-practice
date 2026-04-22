# URL Routing & API Path Guide
## Complete Understanding of How URLs Work in amin_shop_drf

---

## 📌 Table of Contents
1. [URL Routing Flow](#routing-flow)
2. [Main URL Configuration](#main-urls)
3. [API v1 Routing](#api-v1-routing)
4. [ViewSets & Routers](#viewsets--routers)
5. [Nested Routers](#nested-routers)
6. [Complete API Endpoints](#complete-api-endpoints)
7. [How Requests Work](#how-requests-work)
8. [Key Concepts](#key-concepts)

---

## 🔄 Routing Flow

When you make a request to the API, it flows through these layers:

```
User Request (http://localhost:8000/api/v1/products/)
    ↓
amin_shop_main/urls.py (Main URL patterns)
    ↓
api/urls.py (API v1 endpoints)
    ↓
ViewSets (Product, Category, Cart, etc.)
    ↓
Serializers (Convert data to/from JSON)
    ↓
Models (Database operations)
    ↓
Response (JSON back to user)
```

---

## 🎯 Main URL Configuration
### File: `amin_shop_main/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import api_root_view

urlpatterns = [
    path('admin/', admin.site.urls),           # Django admin panel
    path('', api_root_view),                   # Root redirect
    path('api-auth/', include('rest_framework.urls')),  # DRF auth
    path('api/v1/', include('api.urls'), name='api-root')  # API v1
] + debug_toolbar_urls()
```

### Breaking It Down:

| Path | Purpose |
|------|---------|
| `/admin/` | Django admin interface |
| `/api-auth/` | DRF built-in authentication views |
| `/api/v1/` | **All API v1 endpoints** |

**The main entry point is `/api/v1/` which includes all routes from `api/urls.py`**

---

## 🔌 API v1 Routing
### File: `api/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from product.views import ProductViewSet, CategoryViewSets, ReviewViewSet
from rest_framework_nested import routers
from order.views import CartViewSet, CartItemViewSet

# Create a main router
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSets)
router.register('carts', CartViewSet, basename='carts')

# Create nested router for reviews (under products)
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
show how routing works for APIs (DRF)
# Create nested router for cart items (under carts)
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

# Combine all URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls))
]
```

### What Are Routers?

**Routers automatically generate URL patterns from ViewSets.**

Instead of manually writing:
```python
path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', ...})),
```

You just write:
```python
router.register('products', ProductViewSet, basename='products')
```

And the router automatically generates all the standard CRUD URLs!

---

## ⚙️ ViewSets & Routers

### What's a ViewSet?

A **ViewSet** is a class that combines multiple view methods (list, retrieve, create, update, destroy) into a single class.

```python
class ProductViewSet(ModelViewSet):  # ModelViewSet = full CRUD
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
```

**One ViewSet automatically creates:**

| HTTP Method | URL Pattern | ViewSet Method | Operation |
|-------------|-------------|-----------------|-----------|
| `GET` | `/products/` | `list()` | Get all products |
| `POST` | `/products/` | `create()` | Create new product |
| `GET` | `/products/{id}/` | `retrieve()` | Get single product |
| `PUT` | `/products/{id}/` | `update()` | Update product |
| `PATCH` | `/products/{id}/` | `partial_update()` | Partial update |
| `DELETE` | `/products/{id}/` | `destroy()` | Delete product |

### Types of ViewSets:

1. **ModelViewSet** - Full CRUD (Create, Read, Update, Delete)
   ```python
   class ProductViewSet(ModelViewSet):  # All 6 methods available
   ```

2. **ReadOnlyModelViewSet** - Only GET operations
   ```python
   class CategoryViewSets(ReadOnlyModelViewSet):  # Only list & retrieve
   ```

3. **Custom ViewSets** - Mixed operations
   ```python
   class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet, DestroyModelMixin):
       # Only Create, Retrieve, Destroy (no Update or List)
   ```

---

## 🔗 Nested Routers

### What Are Nested Routers?

Nested routers create URLs like `/products/{id}/reviews/` instead of just `/reviews/`.

This shows the relationship between resources.

### Example 1: Product Reviews (Nested)

```python
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
```

**Breakdown:**
- `router` - Parent router (products are registered here)
- `'products'` - Parent resource name
- `lookup='product'` - URL parameter name will be `product_pk`
- `'reviews'` - Child resource name

**Generated URLs:**
```
GET    /api/v1/products/                    # List all products
POST   /api/v1/products/                    # Create product
GET    /api/v1/products/1/                  # Get product 1
GET    /api/v1/products/1/reviews/          # List reviews for product 1
POST   /api/v1/products/1/reviews/          # Create review for product 1
GET    /api/v1/products/1/reviews/5/        # Get review 5 of product 1
PUT    /api/v1/products/1/reviews/5/        # Update review 5
DELETE /api/v1/products/1/reviews/5/        # Delete review 5
```

### Example 2: Cart Items (Nested)

```python
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')
```

**Generated URLs:**
```
GET    /api/v1/carts/                       # List carts
POST   /api/v1/carts/                       # Create cart
GET    /api/v1/carts/{id}/                  # Get specific cart
GET    /api/v1/carts/{id}/items/            # List items in cart
POST   /api/v1/carts/{id}/items/            # Add item to cart
PATCH  /api/v1/carts/{id}/items/{item_id}/ # Update item quantity
DELETE /api/v1/carts/{id}/items/{item_id}/ # Remove item from cart
```

---

## 📋 Complete API Endpoints

### Base URL: `http://localhost:8000/api/v1/`

### Products
```
GET    /products/                    List all products with filtering, search, pagination
POST   /products/                    Create new product
GET    /products/{id}/               Get specific product
PUT    /products/{id}/               Update product (full)
PATCH  /products/{id}/               Update product (partial)
DELETE /products/{id}/               Delete product
```

### Product Reviews (Nested under Products)
```
GET    /products/{product_id}/reviews/                List reviews for product
POST   /products/{product_id}/reviews/                Add review to product
GET    /products/{product_id}/reviews/{review_id}/    Get specific review
PUT    /products/{product_id}/reviews/{review_id}/    Update review
PATCH  /products/{product_id}/reviews/{review_id}/    Partial update review
DELETE /products/{product_id}/reviews/{review_id}/    Delete review
```

### Categories
```
GET    /categories/                  List all categories
POST   /categories/                  Create category
GET    /categories/{id}/             Get specific category
PUT    /categories/{id}/             Update category
PATCH  /categories/{id}/             Update category (partial)
DELETE /categories/{id}/             Delete category
```

### Carts
```
GET    /carts/                       List all carts
POST   /carts/                       Create new cart
GET    /carts/{cart_id}/             Get specific cart details
DELETE /carts/{cart_id}/             Delete cart
```

### Cart Items (Nested under Carts)
```
GET    /carts/{cart_id}/items/                       List items in cart
POST   /carts/{cart_id}/items/                       Add item to cart
GET    /carts/{cart_id}/items/{item_id}/             Get specific item
PATCH  /carts/{cart_id}/items/{item_id}/             Update item quantity
DELETE /carts/{cart_id}/items/{item_id}/             Remove item from cart
```

---

## 🚀 How Requests Work

### Example 1: Get All Products

**Request:**
```
GET http://localhost:8000/api/v1/products/
```

**Flow:**
1. Django matches URL to main `urlpatterns` in `amin_shop_main/urls.py`
2. Finds `path('api/v1/', include('api.urls'))` - passes control to `api/urls.py`
3. Router finds `router.register('products', ProductViewSet)` 
4. Router matches `GET /products/` to `ProductViewSet.list()` method
5. ViewSet queryset returns all products
6. Serializer converts products to JSON
7. Response sent back with list of products

**Response (Example):**
```json
{
  "count": 50,
  "next": "http://localhost:8000/api/v1/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 999.99,
      "stock": 5,
      "category": 1
    },
    ...
  ]
}
```

---

### Example 2: Add Item to Cart

**Request:**
```
POST http://localhost:8000/api/v1/carts/abc-123-uuid/items/

Body (JSON):
{
  "product_id": 1,
  "quantity": 2
}
```

**Flow:**
1. Django matches to `api/urls.py`
2. `cart_router` matches `carts/{cart_pk}/items/`
3. URL parameter `cart_pk = "abc-123-uuid"` extracted
4. Passed to `CartItemViewSet`
5. `create()` method called
6. `AddCartItemSerializer` is used (because it's POST)
7. Serializer validates product exists
8. Creates/updates CartItem in database
9. Returns created item with product details

**Response:**
```json
{
  "id": 15,
  "product_id": 1,
  "quantity": 2
}
```

---

### Example 3: Get Reviews for Specific Product

**Request:**
```
GET http://localhost:8000/api/v1/products/1/reviews/
```

**Flow:**
1. Django routes to `api/urls.py`
2. `product_router` matches `products/{product_pk}/reviews/`
3. Extracts `product_pk = 1` from URL
4. `ReviewViewSet.list()` is called
5. ViewSet context receives `kwargs = {'product_pk': 1}`
6. `get_queryset()` filters: `Review.objects.filter(product_id=1)`
7. Only reviews for product 1 are returned
8. Serialized to JSON

**Response:**
```json
[
  {
    "id": 1,
    "product": 1,
    "name": "John Doe",
    "description": "Great product!",
    "date": "2024-04-20"
  },
  ...
]
```

---

## 🎓 Key Concepts

### 1. **URL Parameters (Path Parameters)**

```
/api/v1/products/123/reviews/5/
         ↑      ↑         ↑
         |      |         |
      resource product_pk review_pk
```

These are captured as `kwargs` in the ViewSet:
```python
def get_queryset(self):
    product_pk = self.kwargs['product_pk']  # Gets 123
    return Review.objects.filter(product_id=product_pk)
```

### 2. **Query Parameters (Query Strings)**

```
/api/v1/products/?category=2&search=laptop&ordering=-price&page=1
               ↑
           Base URL
           
Query parameters:
- ?category=2           Filter by category
- &search=laptop        Search by name
- &ordering=-price      Sort by price (descending)
- &page=1              Pagination
```

Accessed via `self.request.query_params` in ViewSet.

### 3. **HTTP Methods (Verbs)**

| Method | Purpose | Safe | Idempotent |
|--------|---------|------|-----------|
| GET | Retrieve data | ✅ | ✅ |
| POST | Create new data | ❌ | ❌ |
| PUT | Replace entire resource | ❌ | ✅ |
| PATCH | Partial update | ❌ | ✅ |
| DELETE | Remove resource | ❌ | ✅ |

### 4. **Status Codes**

```
200 OK - Request successful
201 Created - Resource created (POST)
204 No Content - Delete successful
400 Bad Request - Invalid data
401 Unauthorized - Not authenticated
403 Forbidden - No permission
404 Not Found - Resource doesn't exist
500 Server Error - Internal server error
```

### 5. **Serializers**

Convert between:
- **Python objects** ↔ **JSON**

Different serializers for different operations:
```python
def get_serializer_class(self):
    if self.request.method == 'POST':
        return AddCartItemSerializer      # For creating
    elif self.request.method == 'PATCH':
        return UpdateCartItemSerializer   # For updating
    return CartItemSerializer             # For retrieving
```

### 6. **Lookup vs Basename**

```python
router.register('products', ProductViewSet, basename='products')
                ↑                           ↑
             URL path              Name for reverse URLs
```

Used to reverse generate URLs:
```python
reverse('products-list')      # /products/
reverse('products-detail', args=[1])  # /products/1/
```

---

## 📊 Routing Decision Tree

When a request comes in, Django makes these decisions:

```
Request: GET /api/v1/products/1/reviews/

↓ Match main URLs

Is it /admin/? NO
Is it /api-auth/? NO
Is it /api/v1/? YES → include('api.urls')

↓ Now in api/urls.py routers

Check main router:
  - /products/? Match! (ProductViewSet)
  - /categories/? No
  - /carts/? No

Check product_router (nested):
  - /products/1/reviews/? Match! (ReviewViewSet)
  - Lookup: product_pk = 1

Check cart_router:
  - /carts/X/items/? No

↓ Found: ReviewViewSet with product_pk=1

Is method GET with detail? YES → retrieve()
Is method GET without detail? → list()

↓ Execute ViewSet method

get_queryset() → Review.objects.filter(product_id=1)
Return serialized response
```

---

## ✅ Summary

- **`amin_shop_main/urls.py`** - Main entry point, routes `/api/v1/` to API
- **`api/urls.py`** - Creates routers and registers ViewSets
- **Routers** - Auto-generate CRUD URLs from ViewSets
- **Nested Routers** - Create dependent URL patterns (product → reviews)
- **ViewSets** - Handle list, create, retrieve, update, delete
- **Serializers** - Convert data to/from JSON

---

## 🔍 Common Routing Patterns

### Pattern 1: Resource with Related Items
```
/products/{id}/reviews/
/products/{id}/reviews/{review_id}/
```

### Pattern 2: User's Data
```
/users/{id}/orders/
/users/{id}/orders/{order_id}/
```

### Pattern 3: Collections
```
/categories/
/categories/{id}/products/
```

### Pattern 4: Actions
```
GET    /products/                    # List
POST   /products/                    # Create
GET    /products/{id}/               # Retrieve
PUT    /products/{id}/               # Full update
PATCH  /products/{id}/               # Partial update
DELETE /products/{id}/               # Delete
```

All generated automatically by routers! 🎉
