# RESTful GET API with Flask

A RESTful API built with Flask that provides product information with filtering capabilities. Demonstrates REST conventions, JSON responses, and query parameter handling.

## Features

- 🏠 **API Homepage** - Welcome message with endpoint documentation
- 📦 **Product Listing** - Retrieve all products as JSON
- 🔍 **Category Filtering** - Filter products by category using query parameters
- 🎯 **Single Product Retrieval** - Get specific product by ID
- ✅ **Proper Status Codes** - Returns 200 for success, 404 for not found
- 📊 **JSON Responses** - All data returned in JSON format

## Technologies Used

- **Python 3.12** - Core programming language
- **Flask** - Web framework for API development
- **Pipenv** - Dependency and virtual environment management

## Setup

### Prerequisites
- Python 3.12
- Pipenv

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd python-flask-restful-get-apis-lab

# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell

# Run the application
python app.py
```

The server will start on `http://127.0.0.1:5000`

## API Endpoints

### 1. Homepage - API Documentation
```
GET /
```

**Description:** Returns welcome message and available endpoints.

**Response:**
```json
{
  "message": "Welcome to the Products API",
  "endpoints": {
    "GET /": "This welcome message",
    "GET /products": "List all products (optional ?category=electronics filter)",
    "GET /products/<id>": "Get a specific product by ID"
  }
}
```

**Example:**
```bash
curl http://127.0.0.1:5000/
```

---

### 2. Get All Products
```
GET /products
```

**Description:** Returns all products in the catalog.

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 899.99,
    "category": "electronics"
  },
  {
    "id": 2,
    "name": "Book",
    "price": 14.99,
    "category": "books"
  },
  {
    "id": 3,
    "name": "Desk",
    "price": 199.99,
    "category": "furniture"
  }
]
```

**Example:**
```bash
curl http://127.0.0.1:5000/products
```

---

### 3. Filter Products by Category
```
GET /products?category={category_name}
```

**Description:** Returns products filtered by category (case-insensitive).

**Query Parameters:**
- `category` (string) - Category to filter by (e.g., "electronics", "books", "furniture")

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 899.99,
    "category": "electronics"
  }
]
```

**Examples:**
```bash
# Get electronics products
curl http://127.0.0.1:5000/products?category=electronics

# Get books
curl http://127.0.0.1:5000/products?category=books

# Get furniture
curl http://127.0.0.1:5000/products?category=furniture
```

---

### 4. Get Product by ID
```
GET /products/<id>
```

**Description:** Returns a specific product by its ID.

**Path Parameters:**
- `id` (integer) - Product ID

**Response (Success):** `200 OK`
```json
{
  "id": 2,
  "name": "Book",
  "price": 14.99,
  "category": "books"
}
```

**Response (Not Found):** `404 Not Found`
```json
{
  "error": "Product not found"
}
```

**Examples:**
```bash
# Get product with ID 1
curl http://127.0.0.1:5000/products/1

# Get product with ID 2
curl http://127.0.0.1:5000/products/2

# Try invalid ID (returns 404)
curl -i http://127.0.0.1:5000/products/999
```

---

## Sample Data

The API currently uses mock data with three products:

| ID | Name    | Price   | Category     |
|----|---------|---------|--------------|
| 1  | Laptop  | $899.99 | electronics  |
| 2  | Book    | $14.99  | books        |
| 3  | Desk    | $199.99 | furniture    |

## RESTful Design Principles

This API follows REST conventions:

✅ **Resource-based URLs** - Uses nouns (`/products`), not verbs  
✅ **Plural naming** - `/products` not `/product`  
✅ **HTTP methods** - GET for data retrieval  
✅ **JSON format** - Consistent data format  
✅ **Proper status codes** - 200 for success, 404 for not found  
✅ **Query parameters** - For filtering (`?category=electronics`)  
✅ **Path parameters** - For specific resources (`/products/1`)  

## Testing

### Manual Testing with curl
```bash
# Test all endpoints
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/products
curl http://127.0.0.1:5000/products?category=electronics
curl http://127.0.0.1:5000/products/1
curl -i http://127.0.0.1:5000/products/999
```

### Automated Testing with pytest
```bash
# Run all tests
pytest -v

# Run specific test file
pytest tests/test_app.py -v
```

**Test Coverage:**
- ✅ Homepage returns welcome message
- ✅ Get all products returns list
- ✅ Get product by ID returns correct product
- ✅ Invalid product ID returns 404
- ✅ Category filter returns correct products

## Project Structure
```
python-flask-restful-get-apis-lab/
├── app.py                  # Flask application with API routes
├── tests/
│   └── test_app.py        # Pytest test suite
├── Pipfile                # Python dependencies
├── Pipfile.lock          # Locked dependency versions
└── README.md             # This file
```

## API Response Examples

### Successful Product Retrieval (200)
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 899.99,
  "category": "electronics"
}
```

### Product Not Found (404)
```json
{
  "error": "Product not found"
}
```

### Filtered Results
```json
[
  {
    "id": 2,
    "name": "Book",
    "price": 14.99,
    "category": "books"
  }
]
```

## Future Enhancements

- Add POST endpoint to create new products
- Add PUT/PATCH endpoints to update products
- Add DELETE endpoint to remove products
- Implement pagination for large datasets
- Add database integration (SQLAlchemy)
- Add authentication and authorization
- Add input validation with schema validators
- Implement error handling middleware
- Add API versioning (e.g., `/api/v1/products`)
- Add rate limiting

## HTTP Status Codes Used

| Code | Meaning  | When Used |
|------|----------|-----------|
| 200  | OK       | Successful GET request with data |
| 404  | Not Found | Requested product ID doesn't exist |

## Author

**Greg**  
Flatiron School - Flask RESTful API Development Lab  
January 2026

## License

Educational project - Flatiron School Curriculum