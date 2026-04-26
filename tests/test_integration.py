from app import app
import json

def test_create_and_get_products():
    client = app.test_client()

    client.post("/products", json={
        "name": "Laptop",
        "price": 1000,
        "stock": 10
    })

    response = client.get("/products")
    data = response.get_json()

    assert len(data) > 0
    assert data[0]["name"] == "Laptop"
from app import app

def test_order_flow():
    client = app.test_client()

    res = client.post("/order", json={
        "product_id": 1,
        "quantity": 1
    })

    assert res.status_code in [200, 400, 404]