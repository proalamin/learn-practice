# Quick Learning Path - URL Routing

## Visual Progression Guide

---

## 🚀 Your Learning Journey

```
START HERE
    ↓
Step 1: URL Basics (5 min)
    ↓
Step 2: Django path() (5 min)
    ↓
Step 3: Path Parameters <int:pk> (5 min)
    ↓
Step 4: Class-Based Views (5 min)
    ↓
Step 5: ViewSets (5 min)
    ↓
Step 6: Simple Routers (5 min)
    ↓
Step 7: Nested Routers ⭐ (KEY CONCEPT) (5 min)
    ↓
Step 8: Advanced Patterns (5 min)
    ↓
YOU ARE AN EXPERT! 🎉
```

---

## 📊 Progression Diagram

### What You'll Understand at Each Step

```
STEP 1: URL BASICS
├─ http://localhost:8000/api/v1/products/
├─ What is a URL path
└─ What is a query string

STEP 2: DJANGO PATTERNS
├─ path('products/', views.products)
├─ path('reviews/', views.reviews)
├─ Multiple patterns
└─ Include patterns

STEP 3: PATH PARAMETERS
├─ path('products/<int:pk>/', views.product_detail)
├─ <int:pk> extracts ID from URL
├─ Can use: <int:id>, <str:name>, <uuid:id>
└─ Multiple parameters possible

STEP 4: CLASS-BASED VIEWS
├─ class ProductList(APIView):
│  ├─ def get(self, request): ...
│  └─ def post(self, request): ...
├─ One class handles multiple methods
└─ Cleaner than function-based views

STEP 5: VIEWSETS
├─ class ProductViewSet(ModelViewSet):
│  └─ Automatically has:
│     ├─ list()              GET /products/
│     ├─ create()            POST /products/
│     ├─ retrieve()          GET /products/{pk}/
│     ├─ update()            PUT /products/{pk}/
│     ├─ partial_update()    PATCH /products/{pk}/
│     └─ destroy()           DELETE /products/{pk}/
├─ ONE class = 6 URLs!
└─ Much less code

STEP 6: ROUTERS
├─ router = DefaultRouter()
├─ router.register('products', ProductViewSet)
│  └─ Automatically generates all 6 URLs above!
├─ ONE line of code = 6 URLs
└─ Routers auto-inspect ViewSets

STEP 7: NESTED ROUTERS ⭐
├─ products_router = NestedDefaultRouter(router, 'products', lookup='product')
├─ products_router.register('reviews', ReviewViewSet)
│  └─ Creates:
│     ├─ /products/1/reviews/        (reviews for product 1)
│     ├─ /products/1/reviews/5/      (review 5 of product 1)
│     ├─ /products/2/reviews/        (reviews for product 2)
│     └─ etc.
├─ Parent-child relationships in URLs
└─ Filters automatically via get_queryset()

STEP 8: ADVANCED
├─ Multi-level nesting
│  └─ /users/1/orders/5/items/10/
├─ Custom actions
│  └─ @action decorator for /products/popular/
├─ Query parameters
│  └─ /products/?search=laptop&category=1
└─ Complex filtering
```

---

## 🎯 Key Concepts per Step

| Step | Concept      | Key Idea         | Code                     |
| ---- | ------------ | ---------------- | ------------------------ |
| 1    | URLs         | Address on web   | http://...               |
| 2    | Patterns     | Map URL to view  | `path('products/', ...)` |
| 3    | Parameters   | Extract ID       | `<int:pk>`               |
| 4    | CBV          | Class methods    | `class View(APIView):`   |
| 5    | ViewSet      | Combined CRUD    | `ModelViewSet`           |
| 6    | Router       | Auto URLs        | `router.register()`      |
| 7    | NestedRouter | Parent-child     | `/products/1/reviews/`   |
| 8    | Advanced     | Complex patterns | Custom actions           |

---

## 📝 Real Code at Each Step

### Step 1-2: Basic Pattern

```python
# urls.py
urlpatterns = [
    path('products/', views.products),
]
```

### Step 2-3: With Parameters

```python
# urls.py
urlpatterns = [
    path('products/', views.products),
    path('products/<int:pk>/', views.product_detail),
]
```

### Step 4: Class-Based View

```python
# views.py
class ProductList(APIView):
    def get(self, request):
        return Response(...)
    def post(self, request):
        return Response(...)

# urls.py
urlpatterns = [
    path('products/', ProductList.as_view()),
]
```

### Step 5: ViewSet (Replaces above!)

```python
# views.py
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

# Only needs registration, not multiple paths!
```

### Step 6: Router (Replaces manual paths!)

```python
# urls.py
router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls  # That's it! 6 URLs generated!
```

### Step 7: Nested Router (Parent-child URLs)

```python
# urls.py
router = DefaultRouter()
router.register('products', ProductViewSet)

reviews_router = NestedDefaultRouter(
    router,
    'products',
    lookup='product'
)
reviews_router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(reviews_router.urls)),
]

# Generates: /products/1/reviews/, /products/1/reviews/5/, etc.
```

### Step 8: Advanced (Custom Actions)

```python
class ProductViewSet(ModelViewSet):
    @action(detail=False, methods=['get'])
    def popular(self, request):
        return Response(...)

# Generates: GET /products/popular/
```

---

## 🔄 Evolution of Code Complexity

### Concept: Get a Product Detail

**Step 2 (Manual, Verbose):**

```python
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)
```

**Step 4 (Class-based, cleaner):**

```python
class ProductDetail(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return Response(ProductSerializer(product).data)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Product.objects.get(pk=pk).delete()
        return Response(status=204)
```

**Step 5-6 (ViewSet + Router, automated!):**

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

# Register with router - all 6 operations handled automatically!
router.register('products', ProductViewSet)
```

**95% less code!** 🎉

---

## 📚 When to Read What

| You Want To...        | Read This | Time   |
| --------------------- | --------- | ------ |
| Understand URL basics | Step 1-3  | 15 min |
| Learn ViewSets        | Step 4-5  | 15 min |
| Learn Routers         | Step 6    | 10 min |
| Learn Nested Routers  | Step 7    | 10 min |
| Advanced stuff        | Step 8    | 10 min |
| Everything            | All steps | 60 min |

---

## 🎓 Quick Test: Can You?

After each step, you should be able to:

**After Step 1-2:**

- [ ] Understand URL structure
- [ ] Write basic `path()` patterns

**After Step 3:**

- [ ] Extract parameters from URLs
- [ ] Use `<int:pk>` in patterns

**After Step 4:**

- [ ] Use APIView class
- [ ] Map HTTP methods to class methods

**After Step 5:**

- [ ] Know what a ViewSet is
- [ ] Understand it has 6 automatic methods

**After Step 6:**

- [ ] Register ViewSet with router
- [ ] Know router auto-generates URLs

**After Step 7:**

- [ ] Create nested URLs (parent/child)
- [ ] Know lookup parameter behavior
- [ ] Filter nested resources

**After Step 8:**

- [ ] Create custom actions
- [ ] Handle complex relationships
- [ ] Optimize queries

---

## 💡 Pro Tips for Learning

1. **Code as you learn** - Don't just read, write code
2. **Test each step** - Use curl/Postman to test URLs
3. **Look at your project** - See real examples in `api/urls.py`
4. **Trace a request** - Follow how `/api/v1/products/1/reviews/` is handled
5. **Start simple** - Create a simple ViewSet before nested ones

---

## 🔗 Document Mapping

| Step | Document                                                |
| ---- | ------------------------------------------------------- |
| 1-3  | ROUTING_LEARNING_PATH.md (Steps 1-3)                    |
| 4-5  | VIEWSETS_MIXINS_GENERICS.md                             |
| 6-7  | ROUTING_LEARNING_PATH.md (Steps 6-7) + ROUTING_GUIDE.md |
| 8    | ROUTING_LEARNING_PATH.md (Step 8)                       |
| All  | ROUTING_LEARNING_PATH.md                                |

---

## 🚀 Your Action Plan

1. **Read ROUTING_LEARNING_PATH.md** (45 min)
   - Go through all 8 steps
   - Don't skip any step
   - Try the practice exercises

2. **Open your project** (5 min)
   - Look at `api/urls.py`
   - See how it uses routers
   - Find the nested routers

3. **Test with cURL** (10 min)
   - Test endpoints from API_EXAMPLES.md
   - See URLs working in practice

4. **Trace a request** (10 min)
   - Pick a URL: `/api/v1/products/1/reviews/5/`
   - Trace how it's handled step-by-step
   - See each layer (router → viewset → serializer)

5. **Create something** (20 min)
   - Add a new ViewSet
   - Register it with router
   - Test the generated URLs

---

## ✨ Success Criteria

You've learned routing when you can:

1. ✅ Explain what a router does
2. ✅ Predict what URLs a ViewSet generates
3. ✅ Understand nested router parent-child relationships
4. ✅ Filter nested resources in `get_queryset()`
5. ✅ Create multi-level nested URLs
6. ✅ Add custom actions with `@action`
7. ✅ Trace a request through the entire system

---

## 🎉 You're Ready!

Start with **ROUTING_LEARNING_PATH.md** and follow the steps.

Each step builds on the previous one. Don't skip ahead!

**Happy Learning! 🚀**
