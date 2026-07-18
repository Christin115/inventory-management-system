from flask import Blueprint, jsonify, request
from models import db
from models.item import Item
from services.food_api import get_product_by_barcode

inventory_bp = Blueprint("inventory", __name__)


# -----------------------
# HOME
# -----------------------

@inventory_bp.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API",
        "routes": [
            "/items",
            "/items/<id>",
            "/search?name=",
            "/low-stock",
            "/import/<barcode>"
        ]
    })


# -----------------------
# GET ALL ITEMS
# -----------------------

@inventory_bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])


# -----------------------
# GET ONE ITEM
# -----------------------

@inventory_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())


# -----------------------
# CREATE ITEM
# -----------------------

@inventory_bp.route("/items", methods=["POST"])
def create_item():

    data = request.get_json()

    item = Item(
        name=data["name"],
        barcode=data.get("barcode"),
        brand=data.get("brand"),
        category=data.get("category"),
        package_size=data.get("package_size"),
        origin=data.get("origin"),
        image_url=data.get("image_url"),
        quantity=data.get("quantity", 0),
        price=data.get("price", 0.0)
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_dict()), 201


# -----------------------
# UPDATE ITEM
# -----------------------

@inventory_bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):

    item = Item.query.get_or_404(item_id)

    data = request.get_json()

    item.name = data.get("name", item.name)
    item.barcode = data.get("barcode", item.barcode)
    item.brand = data.get("brand", item.brand)
    item.category = data.get("category", item.category)
    item.package_size = data.get("package_size", item.package_size)
    item.origin = data.get("origin", item.origin)
    item.image_url = data.get("image_url", item.image_url)
    item.quantity = data.get("quantity", item.quantity)
    item.price = data.get("price", item.price)

    db.session.commit()

    return jsonify(item.to_dict())


# -----------------------
# DELETE ITEM
# -----------------------

@inventory_bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    item = Item.query.get_or_404(item_id)

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item deleted"})


# -----------------------
# SEARCH
# -----------------------

@inventory_bp.route("/search", methods=["GET"])
def search_items():

    name = request.args.get("name")

    if not name:
        return jsonify([])

    items = Item.query.filter(Item.name.ilike(f"%{name}%")).all()

    return jsonify([item.to_dict() for item in items])


# -----------------------
# LOW STOCK
# -----------------------

@inventory_bp.route("/low-stock", methods=["GET"])
def low_stock():

    items = Item.query.filter(Item.quantity < 5).all()

    return jsonify([item.to_dict() for item in items])


# -----------------------
# IMPORT FROM OPEN FOOD FACTS
# -----------------------

@inventory_bp.route("/import/<barcode>", methods=["POST"])
def import_product(barcode):

    product = get_product_by_barcode(barcode)

    print("\n========== PRODUCT FROM API ==========")
    print(product)
    print("======================================\n")

    if not product:
        return jsonify({"error": "Product not found"}), 404

    existing = Item.query.filter_by(barcode=product["barcode"]).first()

    if existing:
        return jsonify({"error": "Item already exists"}), 409

    item = Item(
        name=product["name"],
        barcode=product["barcode"],
        brand=product["brand"],
        category=product["category"],
        package_size=product["package_size"],
        origin=product["origin"],
        image_url=product["image_url"],
        quantity=1,
        price=0.0
    )

    db.session.add(item)
    db.session.commit()

    print("\n========== ITEM SAVED ==========")
    print(item.to_dict())
    print("================================\n")

    return jsonify(item.to_dict()), 201