from models import Product

def test_product_logic():
    p = Product(name="Phone", price=100, stock=5)

    assert p.price == 100
    assert p.stock == 5