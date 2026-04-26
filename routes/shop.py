from flask import Blueprint, jsonify, request
from models import Product, Order
from db import db

shop_bp = Blueprint("shop", __name__)

# Create product
@shop_bp.route("/products", methods=["POST"])
def create_product():
    data = request.json
    p = Product(name=data["name"], price=data["price"], stock=data["stock"])
    db.session.add(p)
    db.session.commit()
    return jsonify({"message": "Product created"}), 201


# Get all products
@shop_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "price": p.price, "stock": p.stock}
        for p in products
    ])


# Place order
@shop_bp.route("/order", methods=["POST"])
def create_order():
    data = request.json

    if "product_id" not in data or "quantity" not in data:
        return jsonify({"error": "Missing fields"}), 400

    product = Product.query.get(data["product_id"])

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if data["quantity"] <= 0:
        return jsonify({"error": "Invalid quantity"}), 400

    if product.stock < data["quantity"]:
        return jsonify({"error": "Out of stock"}), 400

    total = product.price * data["quantity"]
    product.stock -= data["quantity"]

    db.session.commit()

    return jsonify({
        "message": "Order placed",
        "product": product.name,
        "total": total
    })