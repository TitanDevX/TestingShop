from flask import Flask, render_template, request, jsonify
from db import db
from routes.shop import shop_bp
from models import Product

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(shop_bp)

@app.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)

with app.app_context():
    db.create_all()
    with app.app_context():
     if Product.query.count() == 0:
        db.session.add(Product(name="Phone", price=500, stock=10))
        db.session.add(Product(name="Laptop", price=1200, stock=5))
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)