# Django REST Framework Cheat Sheet

## Quick Reference Guide

---

## 📋 URL Structure Quick Reference

### Main Entry Point

```
http://localhost:8000/api/v1/
```

### All Available Endpoints

```
┌─ PRODUCTS
│  GET    /products/                              List all
│  POST   /products/                              Create
│  GET    /products/{id}/                         Get one
│  PUT    /products/{id}/                         Full update
│  PATCH  /products/{id}/                         Partial update
│  DELETE /products/{id}/                         Delete
│
├─ PRODUCT REVIEWS (Nested)
│  GET    /products/{product_id}/reviews/         List reviews
│  POST   /products/{product_id}/reviews/         Add review
│  GET    /products/{product_id}/reviews/{id}/    Get review
│  PUT    /products/{product_id}/reviews/{id}/    Update review
│  PATCH  /products/{product_id}/reviews/{id}/    Partial update
│  DELETE /products/{product_id}/reviews/{id}/    Delete review
│
├─ CATEGORIES
│  GET    /categories/                            List all
│  POST   /categories/                            Create
│  GET    /categories/{id}/                       Get one
│  PUT    /categories/{id}/                       Full update
│  PATCH  /categories/{id}/                       Partial update
│  DELETE /categories/{id}/                       Delete
│
├─ CARTS
│  GET    /carts/                                 NOT available
│  POST   /carts/                                 Create cart
│  GET    /carts/{id}/                            Get cart details
│  DELETE /carts/{id}/                            Delete cart
│
└─ CART ITEMS (Nested)
   GET    /carts/{cart_id}/items/                 List items
   POST   /carts/{cart_id}/items/                 Add item
   GET    /carts/{cart_id}/items/{id}/            Get item
   PATCH  /carts/{cart_id}/items/{id}/            Update quantity
   DELETE /carts/{cart_id}/items/{id}/            Remove item
```

---

## 🔍 Query Parameters

### Pagination

```
?page=1              # Go to page 1
?page_size=50        # Items per page
```

### Filtering

```
?category=1          # Filter by category
?search=laptop       # Search products
?ordering=price      # Sort by price (ascending)
?ordering=-price     # Sort by price (descending)
?ordering=-id        # Sort by ID descending
```

### Combined Example

```
/products/?category=1&search=gaming&ordering=-price&page=1
```

---

## 🛠️ HTTP Methods Cheat Sheet

| Method | Purpose        | URL Pattern                       | Example            |
| ------ | -------------- | --------------------------------- | ------------------ |
| GET    | Read           | `/endpoint/` or `/endpoint/{id}/` | Get products list  |
| POST   | Create         | `/endpoint/`                      | Create new product |
| PUT    | Full Update    | `/endpoint/{id}/`                 | Replace product    |
| PATCH  | Partial Update | `/endpoint/{id}/`                 | Update only price  |
| DELETE | Delete         | `/endpoint/{id}/`                 | Remove product     |

---

## 📦 HTTP Status Codes

| Code | Meaning            | Use Case                      |
| ---- | ------------------ | ----------------------------- |
| 200  | OK                 | GET, PUT, PATCH successful    |
| 201  | Created            | POST successful               |
| 204  | No Content         | DELETE successful             |
| 400  | Bad Request        | Invalid data/validation error |
| 404  | Not Found          | Resource doesn't exist        |
| 405  | Method Not Allowed | HTTP method not supported     |
| 500  | Server Error       | Internal server error         |

---

## 🔑 Key Files & Locations

```
amin_shop_drf/
├─ amin_shop_main/
│  ├─ urls.py              # Main URL router → /api/v1/
│  ├─ settings.py          # Django settings
│  └─ views.py             # Root view
│
├─ api/
│  └─ urls.py              # API v1 router setup
│
├─ product/
│  ├─ models.py            # Product, Category, Review models
│  ├─ views.py             # ProductViewSet, CategoryViewSet
│  ├─ serializers.py       # ProductSerializers, CategorySerializer
│  ├─ product_urls.py      # Older URL config (not used)
│  ├─ categories_urls.py   # Older URL config (not used)
│  ├─ filters.py           # ProductFilter for filtering
│  └─ paginations.py       # DefaultPagination
│
├─ order/
│  ├─ models.py            # Cart, CartItem, Order, OrderItem models
│  ├─ views.py             # CartViewSet, CartItemViewSet
│  ├─ serializers.py       # Cart, CartItem serializers
│
├─ users/
│  ├─ models.py            # Custom User model
│  ├─ managers.py          # CustomUserManager
│
├─ db.sqlite3              # SQLite database
├─ manage.py               # Django management
└─ doc/                    # Documentation (YOU ARE HERE)
   ├─ ROUTING_GUIDE.md
   ├─ REQUEST_RESPONSE_FLOW.md
   ├─ API_EXAMPLES.md
   ├─ VIEWSETS_MIXINS_GENERICS.md
   └─ CHEAT_SHEET.md (this file)
```

---

## 🎯 Routing Flow Diagram

```
Request: GET /api/v1/products/1/

        ↓

amin_shop_main/urls.py
    path('api/v1/', include('api.urls'))

        ↓

api/urls.py
    router.register('products', ProductViewSet)

        ↓

Router auto-generates:
    GET /products/          → ProductViewSet.list()
    GET /products/{id}/     → ProductViewSet.retrieve()
    POST /products/         → ProductViewSet.create()
    PUT /products/{id}/     → ProductViewSet.update()
    PATCH /products/{id}/   → ProductViewSet.partial_update()
    DELETE /products/{id}/  → ProductViewSet.destroy()

        ↓

ProductViewSet handles request

        ↓

Serializer validates data

        ↓

Model performs database operation

        ↓

Response returned to client
```

---

## 🔄 Request/Response Cycle (Simplified)

```
1. CLIENT REQUEST
   POST /api/v1/products/
   { "name": "Laptop", "price": 999.99, ... }

2. URL ROUTING
   Matched to ProductViewSet.create()

3. DESERIALIZATION
   JSON → ProductSerializers

4. VALIDATION
   Check data is valid

5. SAVE
   Model.objects.create()

6. SERIALIZATION
   Product instance → ProductSerializers → JSON

7. RESPONSE
   201 Created
   { "id": 1, "name": "Laptop", "price": "999.99", ... }
```

---

## 📝 Common ViewSet Patterns

### Full CRUD (Create, Read, Update, Delete)

```python
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
```

**Provides:** GET list, POST create, GET detail, PUT update, PATCH partial_update, DELETE

---

### Read-Only

```python
from rest_framework.viewsets import ReadOnlyModelViewSet

class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
```

**Provides:** GET list, GET detail only

---

### Custom Mix

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class CartViewSet(
    mixins.CreateModelMixin,     # POST /
    mixins.RetrieveModelMixin,   # GET /{id}/
    mixins.DestroyModelMixin,    # DELETE /{id}/
    GenericViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
```

**Provides:** POST create, GET detail, DELETE destroy

---

## 🔗 Nested Router Pattern

```python
# Main router
router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

# Nested router
product_router = NestedDefaultRouter(
    router,           # Parent router
    'products',       # Parent resource name
    lookup='product'  # URL param name: product_pk
)
product_router.register('reviews', ReviewViewSet, basename='product-review')

# Generates URLs:
# /products/
# /products/{product_pk}/reviews/
# /products/{product_pk}/reviews/{review_pk}/
```

---

## 🔐 Common ViewSet Customizations

### Override get_queryset()

```python
def get_queryset(self):
    """Filter based on user or other criteria"""
    queryset = super().get_queryset()
    category = self.request.query_params.get('category')
    if category:
        queryset = queryset.filter(category_id=category)
    return queryset
```

### Override get_serializer_class()

```python
def get_serializer_class(self):
    """Different serializer per method"""
    if self.request.method == 'POST':
        return ProductCreateSerializer
    return ProductDetailSerializer
```

### Override perform_create()

```python
def perform_create(self, serializer):
    """Custom logic before save"""
    serializer.save(owner=self.request.user)
```

### Custom Actions

```python
from rest_framework.decorators import action

@action(detail=False, methods=['get'])
def popular(self, request):
    """GET /products/popular/"""
    popular = Product.objects.filter(rating__gte=4)
    serializer = self.get_serializer(popular, many=True)
    return Response(serializer.data)
```

---

## 📊 Serializer Quick Guide

### ModelSerializer (Most Common)

```python
class ProductSerializers(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'price_with_tax', 'stock']

    def get_price_with_tax(self, obj):
        return obj.price * 1.1
```

### Field Validation

```python
def validate_price(self, value):
    if value < 0:
        raise serializers.ValidationError("Price must be positive")
    return value
```

### Object Validation

```python
def validate(self, data):
    if data['price'] > 10000 and data['stock'] < 5:
        raise serializers.ValidationError("Check your data")
    return data
```

### Nested Serializer

```python
class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
```

---

## 🎓 Learning Resources in This Project

1. **ROUTING_GUIDE.md** - How URLs are structured and routed
2. **REQUEST_RESPONSE_FLOW.md** - Data flow from request to response
3. **API_EXAMPLES.md** - Real API calls with cURL and Postman
4. **VIEWSETS_MIXINS_GENERICS.md** - Deep dive into views
5. **CHEAT_SHEET.md** - This quick reference

---

## 🚀 Quick Start Template

### Create New API Endpoint

**1. Create Model** (`product/models.py`)

```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

**2. Create Serializer** (`product/serializers.py`)

```python
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
```

**3. Create ViewSet** (`product/views.py`)

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
```

**4. Register in Router** (`api/urls.py`)

```python
router.register('products', ProductViewSet, basename='products')
```

**Done!** Automatic URLs:

```
GET    /api/v1/products/
POST   /api/v1/products/
GET    /api/v1/products/{id}/
PUT    /api/v1/products/{id}/
PATCH  /api/v1/products/{id}/
DELETE /api/v1/products/{id}/
```

---

## 💡 Common Mistakes & Fixes

### Mistake 1: Forgetting to Register in Router

```python
# ❌ Won't work
class MyViewSet(ModelViewSet):
    pass

# ✅ Register it!
router.register('myendpoint', MyViewSet)
```

### Mistake 2: Wrong Mixin Order

```python
# ❌ Wrong
class MyViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    pass

# ✅ Correct
class MyViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    pass
```

### Mistake 3: Not Passing Context to Serializer

```python
# ❌ Missing context
serializer = MySerializer(data=request.data)

# ✅ Include context
serializer = MySerializer(
    data=request.data,
    context={'request': request, 'cart_id': cart_id}
)
```

### Mistake 4: Invalid Nested Router Setup

```python
# ❌ Wrong - need to include nested router URLs
urlpatterns = [path('', include(router.urls))]

# ✅ Correct
urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls))
]
```

---

## 🔍 Debugging Tips

### Check Available URLs

```bash
python manage.py show_urls
# or visit http://localhost:8000/api/v1/ in browser
```

### Test with cURL

```bash
curl -X GET http://localhost:8000/api/v1/products/
```

### Use Django Shell

```bash
python manage.py shell
>>> from product.models import Product
>>> Product.objects.all()
```

### Enable Debug Mode

Already enabled in `settings.py`

```python
DEBUG = True
```

---

## 📚 File Reading Order

Start here:

1. This CHEAT_SHEET.md (overview)
2. ROUTING_GUIDE.md (understand URLs)
3. VIEWSETS_MIXINS_GENERICS.md (understand views)
4. REQUEST_RESPONSE_FLOW.md (understand data flow)
5. API_EXAMPLES.md (test with real calls)

---

## ✨ Key Takeaways

1. **Routers auto-generate URLs** from ViewSets
2. **ViewSets combine CRUD** operations
3. **Serializers transform data** (Model ↔ JSON)
4. **Nested routers** create dependent URLs
5. **Mixins** let you customize what methods to include
6. **Filters/Search/Ordering** work with QuerySets

**Remember:** DRF does most of the work for you! 🎉

---

**Questions? Check the detailed guides in the doc folder!**
