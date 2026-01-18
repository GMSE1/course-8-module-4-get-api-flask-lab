from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


@app.route('/')
def home():
    """
    Homepage route - returns a welcome message.
    
    Returns:
        JSON response with welcome message
    """
    return jsonify({
        "message": "Welcome to the Products API",
        "endpoints": {
            "GET /": "This welcome message",
            "GET /products": "List all products (optional ?category=electronics filter)",
            "GET /products/<id>": "Get a specific product by ID"
        }
    })


@app.route('/products')
def get_products():
    """
    GET /products - returns all products or filters by category.
    
    Query Parameters:
        category (optional): Filter products by category
        
    Returns:
        JSON array of products (200)
    """
    # Get optional category query parameter
    category = request.args.get('category')
    
    # If category filter is provided, filter products
    if category:
        filtered_products = [
            product for product in products 
            if product['category'].lower() == category.lower()
        ]
        return jsonify(filtered_products), 200
    
    # Otherwise, return all products
    return jsonify(products), 200


@app.route('/products/<int:id>')
def get_product(id):
    """
    GET /products/<id> - returns a specific product by ID.
    
    Args:
        id: Integer product ID from URL path
        
    Returns:
        JSON product object (200) if found
        JSON error message (404) if not found
    """
    # Search for product with matching ID
    for product in products:
        if product['id'] == id:
            return jsonify(product), 200
    
    # Product not found - return 404
    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)