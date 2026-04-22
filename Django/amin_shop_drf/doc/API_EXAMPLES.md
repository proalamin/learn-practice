# API Testing & Examples Guide

## Practical Examples with Real API Calls

---

## 📌 Table of Contents

1. [Getting Started](#getting-started)
2. [Products API](#products-api)
3. [Categories API](#categories-api)
4. [Cart & Items API](#cart--items-api)
5. [Reviews API](#reviews-api)
6. [Filtering & Search](#filtering--search)
7. [Error Responses](#error-responses)
8. [Using Postman](#using-postman)
9. [Using cURL](#using-curl)

---

## 🚀 Getting Started

### Start the Development Server

```bash
# Activate virtual environment
source .amin_env/bin/activate

# Run migrations (if needed)
python manage.py migrate

# Start server
python manage.py runserver
```

Server runs at: `http://localhost:8000`

### Base URL for All API Calls

```
http://localhost:8000/api/v1/
```

---

## 📦 Products API

### 1. List All Products

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/products/
```

**Response:** `200 OK`

```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Laptop",
      "description": "High-performance laptop",
      "price": "999.99",
      "price_with_tax": "1099.99",
      "stock": 5,
      "category": 1
    },
    {
      "id": 2,
      "name": "Mouse",
      "description": "Wireless mouse",
      "price": "29.99",
      "price_with_tax": "32.99",
      "stock": 50,
      "category": 1
    }
  ]
}
```

---

### 2. Get Specific Product

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/products/1/
```

**Response:** `200 OK`

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": "999.99",
  "price_with_tax": "1099.99",
  "stock": 5,
  "category": 1
}
```

---

### 3. Create New Product

**Request:**

```bash
curl -X POST http://localhost:8000/api/v1/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Keyboard",
    "description": "Mechanical keyboard",
    "price": "149.99",
    "stock": 20,
    "category": 1
  }'
```

**Response:** `201 Created`

```json
{
  "id": 20,
  "name": "Keyboard",
  "description": "Mechanical keyboard",
  "price": "149.99",
  "price_with_tax": "164.99",
  "stock": 20,
  "category": 1
}
```

---

### 4. Update Product (Full)

**Request:**

```bash
curl -X PUT http://localhost:8000/api/v1/products/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gaming Laptop",
    "description": "High-end gaming laptop",
    "price": "1299.99",
    "stock": 3,
    "category": 1
  }'
```

**Response:** `200 OK`

```json
{
  "id": 1,
  "name": "Gaming Laptop",
  "description": "High-end gaming laptop",
  "price": "1299.99",
  "price_with_tax": "1429.99",
  "stock": 3,
  "category": 1
}
```

---

### 5. Partial Update Product

**Request:**

```bash
curl -X PATCH http://localhost:8000/api/v1/products/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "price": "1199.99",
    "stock": 5
  }'
```

**Response:** `200 OK` (Only changed fields shown)

```json
{
  "id": 1,
  "name": "Gaming Laptop",
  "description": "High-end gaming laptop",
  "price": "1199.99",
  "price_with_tax": "1319.99",
  "stock": 5,
  "category": 1
}
```

---

### 6. Delete Product

**Request:**

```bash
curl -X DELETE http://localhost:8000/api/v1/products/1/
```

**Response:** `204 No Content` (Empty response)

---

## 🏷️ Categories API

### 1. List Categories

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/categories/
```

**Response:** `200 OK`

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Electronics",
      "description": "Electronic devices",
      "product_Count": 15
    },
    {
      "id": 2,
      "name": "Accessories",
      "description": "Product accessories",
      "product_Count": 8
    }
  ]
}
```

---

### 2. Get Specific Category

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/categories/1/
```

**Response:** `200 OK`

```json
{
  "id": 1,
  "name": "Electronics",
  "description": "Electronic devices",
  "product_Count": 15
}
```

---

### 3. Create Category

**Request:**

```bash
curl -X POST http://localhost:8000/api/v1/categories/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Software",
    "description": "Software products"
  }'
```

**Response:** `201 Created`

```json
{
  "id": 4,
  "name": "Software",
  "description": "Software products",
  "product_Count": 0
}
```

---

## 🛒 Cart & Items API

### 1. Create Cart for User

**Request:**

```bash
curl -X POST http://localhost:8000/api/v1/carts/ \
  -H "Content-Type: application/json" \
  -d '{
    "user": 1
  }'
```

**Response:** `201 Created`

```json
{
  "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "user": 1,
  "items": [],
  "total_price": 0
}
```

---

### 2. Get Cart Details

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/carts/f47ac10b-58cc-4372-a567-0e02b2c3d479/
```

**Response:** `200 OK`

```json
{
  "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "user": 1,
  "items": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "Laptop",
        "price": "999.99"
      },
      "quantity": 2,
      "total_Price": 1999.98
    }
  ],
  "total_price": 1999.98
}
```

---

### 3. Add Item to Cart

**Request:**

```bash
curl -X POST http://localhost:8000/api/v1/carts/f47ac10b-58cc-4372-a567-0e02b2c3d479/items/ \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "quantity": 2
  }'
```

**Response:** `201 Created`

```json
{
  "id": 1,
  "product_id": 1,
  "quantity": 2
}
```

**If item already exists, quantity is updated automatically**

---

### 4. List Items in Cart

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/carts/f47ac10b-58cc-4372-a567-0e02b2c3d479/items/
```

**Response:** `200 OK`

```json
[
  {
    "id": 1,
    "product": {
      "id": 1,
      "name": "Laptop",
      "price": "999.99"
    },
    "quantity": 2,
    "total_Price": 1999.98
  },
  {
    "id": 2,
    "product": {
      "id": 15,
      "name": "Mouse",
      "price": "29.99"
    },
    "quantity": 1,
    "total_Price": 29.99
  }
]
```

---

### 5. Get Specific Cart Item

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/carts/f47ac10b-58cc-4372-a567-0e02b2c3d479/items/1/
```

**Response:** `200 OK`

```json
{
  "id": 1,
  "product": {
    "id": 1,
    "name": "Laptop",
    "price": "999.99"
  },
  "quantity": 2,
  "total_Price": 1999.98
}
```

---

### 6. Update Item Quantity

**Request:**

```bash
curl -X PATCH http://localhost:8000/api/v1/carts/f47ac10b-58cc-4372-a567-0e02b2c3d479/items/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "quantity": 5
  }'
```

**Response:** `200 OK`

```json
{
  "quantity": 5
}
```

---

### 7. Remove Item from Cart

**Request:**

```bash
curl -X DELETE http://localhost:8000/api/v1/carts/f47ac10b-58cc-4372-a567-0e02b2c3d479/items/1/
```

**Response:** `204 No Content`

---

### 8. Delete Cart

**Request:**

```bash
curl -X DELETE http://localhost:8000/api/v1/carts/f47ac10b-58cc-4372-a567-0e02b2c3d479/
```

**Response:** `204 No Content`

---

## ⭐ Reviews API

### 1. List Reviews for Product

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/products/1/reviews/
```

**Response:** `200 OK`

```json
[
  {
    "id": 1,
    "product": 1,
    "name": "John Doe",
    "description": "Excellent product, very satisfied!",
    "date": "2024-04-20"
  },
  {
    "id": 2,
    "product": 1,
    "name": "Jane Smith",
    "description": "Good quality, fast delivery",
    "date": "2024-04-19"
  }
]
```

---

### 2. Add Review to Product

**Request:**

```bash
curl -X POST http://localhost:8000/api/v1/products/1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alex Johnson",
    "description": "Great product, highly recommended!"
  }'
```

**Response:** `201 Created`

```json
{
  "id": 3,
  "product": 1,
  "name": "Alex Johnson",
  "description": "Great product, highly recommended!",
  "date": "2024-04-20"
}
```

---

### 3. Get Specific Review

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/products/1/reviews/1/
```

**Response:** `200 OK`

```json
{
  "id": 1,
  "product": 1,
  "name": "John Doe",
  "description": "Excellent product, very satisfied!",
  "date": "2024-04-20"
}
```

---

### 4. Update Review

**Request:**

```bash
curl -X PATCH http://localhost:8000/api/v1/products/1/reviews/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Still excellent after 1 year!"
  }'
```

**Response:** `200 OK`

```json
{
  "id": 1,
  "product": 1,
  "name": "John Doe",
  "description": "Still excellent after 1 year!",
  "date": "2024-04-20"
}
```

---

## 🔍 Filtering & Search

### 1. Filter Products by Category

**Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/products/?category=1"
```

**Response:** `200 OK` (Only products in category 1)

---

### 2. Search Products

**Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/products/?search=laptop"
```

**Response:** `200 OK` (Products matching "laptop")

---

### 3. Order/Sort Products

**Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/products/?ordering=-price"
```

**Response:** `200 OK` (Products sorted by price, highest first)

**Other ordering examples:**

```bash
# Sort by price, lowest first
?ordering=price

# Sort by stock
?ordering=stock

# Sort by ID descending
?ordering=-id
```

---

### 4. Pagination

**Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/products/?page=2"
```

**Response:** `200 OK`

```json
{
  "count": 50,
  "next": "http://localhost:8000/api/v1/products/?page=3",
  "previous": "http://localhost:8000/api/v1/products/?page=1",
  "results": [...]
}
```

---

### 5. Combine Multiple Filters

**Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/products/?category=1&search=laptop&ordering=-price&page=1"
```

This gets products:

- In category 1
- Matching "laptop"
- Sorted by price (highest first)
- First page

---

## ❌ Error Responses

### Validation Error (400 Bad Request)

**Request:** (Negative price)

```bash
curl -X POST http://localhost:8000/api/v1/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Product",
    "description": "Test",
    "price": -10,
    "stock": 5,
    "category": 1
  }'
```

**Response:** `400 Bad Request`

```json
{
  "price": ["Price cloud not be negative"]
}
```

---

### Not Found Error (404)

**Request:**

```bash
curl -X GET http://localhost:8000/api/v1/products/999/
```

**Response:** `404 Not Found`

```json
{
  "detail": "Not found."
}
```

---

### Method Not Allowed (405)

**Request:** (Trying to DELETE a category)

```bash
curl -X DELETE http://localhost:8000/api/v1/categories/1/
```

**Response:** `405 Method Not Allowed`

```json
{
  "detail": "Method \"DELETE\" not allowed."
}
```

---

## 🛠️ Using Postman

### 1. Import Collection

Postman can import API collections. Create a new HTTP request:

1. **Click "New Request"**
2. **Set Method:** `GET`, `POST`, `PATCH`, `DELETE`
3. **Set URL:** `http://localhost:8000/api/v1/products/`
4. **Add Headers:**
   ```
   Content-Type: application/json
   ```
5. **Add Body (for POST/PATCH):**
   ```json
   {
     "name": "Product Name",
     "price": 99.99
   }
   ```
6. **Click Send**

---

### 2. Example Postman Flow

**1. Create Product**

- Method: POST
- URL: `http://localhost:8000/api/v1/products/`
- Body:
  ```json
  {
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 999.99,
    "stock": 5,
    "category": 1
  }
  ```

**2. Create Cart**

- Method: POST
- URL: `http://localhost:8000/api/v1/carts/`
- Body:
  ```json
  {
    "user": 1
  }
  ```
- Save response UUID (cart ID)

**3. Add Item to Cart**

- Method: POST
- URL: `http://localhost:8000/api/v1/carts/{CART_ID}/items/`
- Body:
  ```json
  {
    "product_id": 1,
    "quantity": 2
  }
  ```

**4. View Cart**

- Method: GET
- URL: `http://localhost:8000/api/v1/carts/{CART_ID}/`

---

## 💻 Using cURL

### Basic GET

```bash
curl http://localhost:8000/api/v1/products/
```

### With Headers

```bash
curl -H "Content-Type: application/json" http://localhost:8000/api/v1/products/
```

### POST with Data

```bash
curl -X POST http://localhost:8000/api/v1/products/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Product","price":99.99,"stock":5,"category":1}'
```

### PATCH (Partial Update)

```bash
curl -X PATCH http://localhost:8000/api/v1/products/1/ \
  -H "Content-Type: application/json" \
  -d '{"price":79.99}'
```

### DELETE

```bash
curl -X DELETE http://localhost:8000/api/v1/products/1/
```

### Save to Variable (for nested operations)

```bash
# Create cart and save ID
CART_ID=$(curl -X POST http://localhost:8000/api/v1/carts/ \
  -H "Content-Type: application/json" \
  -d '{"user":1}' | grep -o '"id":"[^"]*"' | cut -d'"' -f4)

# Use cart ID
curl -X GET http://localhost:8000/api/v1/carts/$CART_ID/
```

---

## 🎯 Quick Reference

### Create Flow

```bash
# 1. Create cart
CART=$(curl -s -X POST http://localhost:8000/api/v1/carts/ \
  -H "Content-Type: application/json" \
  -d '{"user":1}' | jq -r '.id')

# 2. Add item
curl -X POST http://localhost:8000/api/v1/carts/$CART/items/ \
  -H "Content-Type: application/json" \
  -d '{"product_id":1,"quantity":2}'

# 3. View cart
curl http://localhost:8000/api/v1/carts/$CART/
```

---

## 📊 Status Codes Quick Guide

| Code | Meaning            | When                       |
| ---- | ------------------ | -------------------------- |
| 200  | OK                 | GET, PUT, PATCH successful |
| 201  | Created            | POST successful            |
| 204  | No Content         | DELETE successful          |
| 400  | Bad Request        | Validation error           |
| 404  | Not Found          | Resource doesn't exist     |
| 405  | Method Not Allowed | HTTP method not supported  |
| 500  | Server Error       | Server issue               |

---

**Now you can test any API endpoint! Try them out in Postman or cURL!** 🚀
